from fastapi import FastAPI,Body, Form, Path, Query, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, PlainTextResponse, HTMLResponse, FileResponse, RedirectResponse
from typing import Annotated
from fastapi.templating import Jinja2Templates  
import json

app=FastAPI()
templates=Jinja2Templates(directory="templates")

# 處理 POST 方法的路徑 /signin
@app.post("/signin")    
async def login(
  account:Annotated[str,Form()],
  password:Annotated[str,Form()]):
    if account=="test" and password == "test":
        return {"status":"success"}
    elif account=="" or password == "":
        return {"status":"empty"}
    else:
        return {"status":"error"}

# GET方法將 http://127.0.0.1:8000/member 設為 登入成功畫面
@app.get("/member")
def memberPage():
    return FileResponse("member.html")

# GET方法將/error 設為錯誤頁面
@app.get("/error") # TemplateResponse已經預設 response_class=HTMLResponse，所以可以不用特別寫
async def errorPage(request: Request, message:str="error"): # message為要求字串
    return templates.TemplateResponse("error.html",{"request":request,"message":message})

# 將URL: http://127.0.0.1:8000/設為 index.html
app.mount("/", StaticFiles(directory="public", html=True))