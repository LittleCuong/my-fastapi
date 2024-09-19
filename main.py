# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/new-route")
def new_api():
    return {"message": "Hello, This is new API!"}

@app.get("/geralt")
def geralt_api():
    return {"message": "Geralt Of Rivia!"}

@app.get("/yennefer")
def yen_api():
    return {"message": "Yennefer of Vengerberg"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
