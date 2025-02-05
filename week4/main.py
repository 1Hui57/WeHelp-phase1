from fastapi import FastAPI,Body, Form, Path, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, PlainTextResponse, HTMLResponse, FileResponse, RedirectResponse
from typing import Annotated
import json
app=FastAPI()


# 處理 POST 方法的路徑 /signin
@app.post("/signin")
async def login(
  account:Annotated[str,Form()],
  password:Annotated[str,Form()]
):
    return {"account":account,"password":password}


# 將URL: http://127.0.0.1:8000/設為 index.html
app.mount("/", StaticFiles(directory="public", html=True))
