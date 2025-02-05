from fastapi import FastAPI,Body, Form, Path, Query
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
# return {"account":account,"password":password}

# 將URL: http://127.0.0.1:8000/設為 index.html
app.mount("/", StaticFiles(directory="public", html=True))

# 將 http://127.0.0.1:8000/member 設為 登入成功畫面
@app.get("/member")
def member():
    return FileResponse("member.html")

