from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/ami")
def is_ami(user_id:str):
    result = int(user_id) % 2 == 0
    return {"user_id": user_id, "result": result}