from fastapi import FastAPI, Body, Form, Path, Query, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import (
    FileResponse,
    RedirectResponse,
)
from typing import Annotated
from fastapi.templating import Jinja2Templates

# 驗證使用者狀態
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware

# 建立資料庫連線
import mysql.connector
con=mysql.connector.connect(
    user="root",
    password="123456789",
    host="localhost",
    database="website"
)

app = FastAPI()
templates = Jinja2Templates(directory="templates")
# 設定 Session Middleware，密鑰用來加密 session
app.add_middleware(SessionMiddleware, secret_key="511O1-5111o1")

# 處理POST方法的路徑 /signup
@app.post("/signup")
async def signup(
    request:Request, name:Annotated[str,Form()],account:Annotated[str,Form(),],password:Annotated[str,Form()]
):
    cursor=con.cursor()
    cursor.execute("SELECT username FROM member WHERE username=%s",[account])
    memberData=cursor.fetchone()
    # 比對輸入的帳號是否存在於資料庫內
    # memberData沒有資料時，如果只寫 memberData[0]==account會出現錯誤，因為memberData沒有[0]
    if memberData is not None and memberData[0] ==account:
        # 資料庫已有此筆帳號，進入錯誤頁面並顯示"重複使用者名稱"
        request.session["SIGNED-IN"] = False
        return RedirectResponse("/error?message=重複使用者名稱",status_code=303)
    # 若輸入的帳號不存在資料庫中，則將輸入的名稱、帳號、密碼加進資料庫中
    else:
        cursor.execute("INSERT INTO member (name, username, password) VALUES (%s, %s, %s)", [name, account, password])
        con.commit()
        request.session["SIGNED-IN"] = False
        return RedirectResponse("/",status_code=303)

# 處理 POST 方法的路徑 /signin
@app.post("/signin")
async def login(
    request: Request, signInAccount: Annotated[str, Form()], signInPassword: Annotated[str, Form()]
):
    # 若登入的帳號密碼為資料庫的同一筆資料，則成功登入，並帶有帳號的USER_INFO session
    cursor=con.cursor()
    cursor.execute("SELECT id, name, username FROM member WHERE username=%s AND password=%s",[signInAccount, signInPassword])
    memberData=cursor.fetchone()
    # 當輸入的帳號密碼為資料庫其中一筆，進到登入頁面
    if memberData is not None and memberData[2]==signInAccount:
        # 設定 SIGNED-IN cookie登入狀態時為True
        # 設定 USER_INFO cookie 登入狀態時為 帳號資料
        request.session["SIGNED-IN"] = True
        request.session["USER_INFO"] = {
            "id":memberData[0],
            "name":memberData[1],
            "username":memberData[2]
        }
        return RedirectResponse("/member",status_code=303)    
        # RedirectResponse 預設會用 status_code=307（Temporary Redirect），
        # 這會保持原始請求的方法（也就是 POST），所以 FastAPI 會嘗試用 POST 方法來存取 /member，
        # 但 /member 只接受 GET，因此會回傳 405 Method Not Allowed。
        # 可以明確指定 RedirectResponse 使用 status_code=303（See Other），
        # 這樣瀏覽器會以 GET 方法重新導向 /member
    else:
        request.session["SIGNED-IN"] = False
        return RedirectResponse("/error?message=帳號或密碼輸入錯誤",status_code=303)

# GET方法將 http://127.0.0.1:8000/member 設為 登入成功畫面
@app.get("/member")
def memberPage(
    request: Request,
):
    cursor=con.cursor()
    # 取得資料庫中會員與留言的資料
    cursor.execute("SELECT message.id, message.content, member.name ,member_id FROM message INNER JOIN member ON message.member_id=member.id ORDER BY message.time DESC;")
    messageData=cursor.fetchall()
    con.commit()
    message=[]
    for msg in messageData:
        message.append({"id":msg[0],"content":msg[1],"name":msg[2], "member_id":msg[3]})
    if request.session.get("SIGNED-IN") != True:
        request.session["SIGNED-IN"] = False
        return RedirectResponse("/")
    elif request.session.get("SIGNED-IN") == True and request.session["USER_INFO"]:
        USER_INFO=request.session["USER_INFO"]
        return templates.TemplateResponse(
            "member.html",{"request": request, "USER_INFO":USER_INFO, "message":message}
        )
    else:
        request.session["SIGNED-IN"] = False
        return FileResponse("/")

# GET方法將/error 設為錯誤頁面
@app.get("/error")  
# TemplateResponse已經預設 response_class=HTMLResponse，所以可以不用特別寫
async def errorPage(request: Request, message: str ):  # message為要求字串
    return templates.TemplateResponse(
        "error.html", {"request": request, "message": message}
    )

# GET方法將 /signout 設為回到首頁並設定SIGNED-IN = False，並刪除USER_INFO的session
@app.get("/signout")
async def signout(request: Request):
    request.session["SIGNED-IN"] = False
    del request.session["USER_INFO"]
    return RedirectResponse("/",status_code=303)

# POST 方法設定路徑/createMessage 將使用者輸入的訊息送至後端並串接資料庫
@app.post("/createMessage")
def createMessage(
    request:Request, content:Annotated[str,Form()]
):
    # 拿到使用者狀態中的名字
    user_info=request.session.get("USER_INFO")
    id=user_info["id"]
    cursor=con.cursor()
    cursor.execute("INSERT INTO message (member_id, content) VALUES (%s, %s)", [id, content])
    con.commit()
    return RedirectResponse("/member",status_code=303)

# POST方法設定路徑/deleteMessage 將訊息確認後刪除並返回/member
@app.post("/deleteMessage")
def deleteMessage(
    request:Request, message_id:Annotated[int,Form()]):
    # ,member_id:Annotated[int,Form()]
    cursor=con.cursor()
    USER_INFO=request.session["USER_INFO"]
    # 取得USER_INFO session的會員id
    user_info_id = USER_INFO["id"]
    # 驗證message_id在資料庫中的member_id是否與USER_INFO session的會員id相同
    cursor.execute("SELECT id FROM message WHERE member_id=%s AND id=%s" ,[user_info_id, message_id])
    getMessageId=cursor.fetchone()
    if getMessageId is not None and getMessageId[0]==message_id:
        cursor.execute("DELETE FROM message WHERE id=%s",[message_id])
        con.commit()
        return RedirectResponse("/member",status_code=303)
    else:
        return RedirectResponse("/error?message=無法刪除該留言，請重新登入。",status_code=303)

# GET方法設定路徑/api/member?username=xxxx
@app.get("/api/member")
async def findUserName(
    request:Request, username:str):
    cursor=con.cursor()
    cursor.execute("SELECT id, name, username FROM member WHERE username=%s",[username])
    memberData=cursor.fetchone()
    if memberData is None:
        return {"data":memberData}
    elif memberData is not None:
        return {
            "data":{
                "id":memberData[0],
                "name":memberData[1],
                "username":memberData[2]
            }
        }
# 將URL: http://127.0.0.1:8000/設為 index.html
app.mount("/", StaticFiles(directory="public", html=True))
