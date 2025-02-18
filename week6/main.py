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
    cursor.execute("SELECT * FROM member")
    memberData=cursor.fetchall()
    for element in memberData:
        if element[2]==account:
            request.session["SIGNED-IN"] = False
            return RedirectResponse("/error?message=重複使用者名稱",status_code=303)
        cursor.execute("INSERT INTO member (name, username, password) VALUES (%s, %s, %s)", [name, account, password])
        con.commit()
        request.session["SIGNED-IN"] = False
        return RedirectResponse("/",status_code=303)

# 處理 POST 方法的路徑 /signin
@app.post("/signin")
async def login(
    request: Request, signInAccount: Annotated[str, Form()], signInPassword: Annotated[str, Form()]
):
    cursor=con.cursor()
    cursor.execute("SELECT * FROM member")
    memberData=cursor.fetchall()
    for element in memberData:
        # 當輸入的帳號密碼為資料庫其中一筆，進到登入頁面
        if signInAccount == element[2] and signInPassword == element[3]:
            # 設定 SIGNED-IN cookie登入狀態時為True
            # 設定 USERNAME cookie 登入狀態時為 帳號
            request.session["SIGNED-IN"] = True
            request.session["USER_INFO"] = {
                "id":element[0],
                "name":element[1],
                "username":element[2]
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
    if request.session.get("SIGNED-IN") != True:
        request.session["SIGNED-IN"] = False
        return RedirectResponse("/")
    elif request.session.get("SIGNED-IN") == True and request.session["USER_INFO"]:
        USER_INFO=request.session["USER_INFO"]
        return templates.TemplateResponse(
            "member.html",{"request": request, "USER_INFO":USER_INFO}
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

# GET方法將 /signout 設為回到首頁並設定SIGNED-IN = False
@app.get("/signout")
async def signout(request: Request):
    request.session["SIGNED-IN"] = False
    return RedirectResponse("/",status_code=303)

# GET方法將 /square 設為平方數計算結果頁面
@app.get("/square/{number}")
async def square(request: Request, number: Annotated[int, Path(gt=0)]):
    number = int(number)
    result = number * number
    return templates.TemplateResponse(
        "square.html", {"request": request, "result": result}
    )

# 將URL: http://127.0.0.1:8000/設為 index.html
app.mount("/", StaticFiles(directory="public", html=True))
