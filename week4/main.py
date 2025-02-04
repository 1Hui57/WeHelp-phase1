from fastapi import FastAPI,Body, Form, Path, Query
from fastapi.staticfiles import StaticFiles
from typing import Annotated
import json
app=FastAPI()
# 將URL: http://127.0.0.1:8000/設為 index.html
app.mount("/", StaticFiles(directory="public", html=True))

# 處理 POST 方法的路徑 /signin
@app.post("/signin")
def formData(body=Body(None)):
    # 如果是中文需解碼
    # body=body.decode("utf-8")
    data=json.loads(body)
    return {"ok":True,"method":"POST","result":data}