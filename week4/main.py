from fastapi import FastAPI,Body, Form, Path, Query, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, PlainTextResponse, HTMLResponse, FileResponse, RedirectResponse
from typing import Annotated
from fastapi.templating import Jinja2Templates  
import json
# 驗證使用者狀態
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware

app=FastAPI()
templates=Jinja2Templates(directory="templates")
# 設定 Session Middleware，密鑰用來加密 session
app.add_middleware(SessionMiddleware, secret_key="511O1-5111o1")

# 處理 POST 方法的路徑 /signin
@app.post("/signin")    
async def login(
    request: Request,
    account:Annotated[str,Form()],
    password:Annotated[str,Form()]):
        if account=="test" and password == "test":
            # 設定 SIGNED-IN cookie登入狀態時為True
            request.session["SIGNED-IN"] = True  
            return {"status":"success"}
        elif account=="" or password == "":
            return {"status":"empty"}
        else:
            return {"status":"error"}

# GET方法將 http://127.0.0.1:8000/member 設為 登入成功畫面
@app.get("/member")
def memberPage(request: Request,):
    if request.session.get("SIGNED-IN") != True:
        request.session["SIGNED-IN"] = False
        return RedirectResponse("/")
    return FileResponse("member.html")

# GET方法將/error 設為錯誤頁面
@app.get("/error") # TemplateResponse已經預設 response_class=HTMLResponse，所以可以不用特別寫
async def errorPage(request: Request, message:str="error"): # message為要求字串
    return templates.TemplateResponse("error.html",{"request":request,"message":message})

# GET方法將 /signout 設為回到首頁並設定SIGNED-IN = False
@app.get("/signout")
async def signout(request: Request):
     request.session["SIGNED-IN"] = False
     return RedirectResponse("/")


# 將URL: http://127.0.0.1:8000/設為 index.html
app.mount("/", StaticFiles(directory="public", html=True))