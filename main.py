from fastapi import FastAPI
# from enum import Enum
# from typing import Union
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result

# @app.post("/items/{item_id}")
# async def update_item(item_id: int, item: Item, q: str | None = None):
#     result = {"item_id": item_id, **item.dict()}
#     if q:
#         result.update({"q": q})
#     return result

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# the parameter that is define in in get path are path parameters
# others are query parameters
# using ?q=5 to define the query parameter
# ex: http://localhost:8080/users/1/items/2?q=3&q2=10
# @app.get("/users/{user_id}")
# async def get_user(user_id: int, q: Union[int,None]=None):
#     return {"user_id": user_id, "q": q}

# class UserId(int, Enum):
#     Alice = 1
#     Bob = 2
#     Eve = 3

# @app.get("/users/{user_id}")
# async def get_users(user_id: UserId):
#     if user_id is UserId.Alice: # or "user_id == UserId.Alice"
#         return {"user_id": user_id, "user_info": "someone who wants to send secret to Bob"}
#     if user_id.value == 2:
#         return {"user_id": user_id, "user_info": "someone who can access Alice's secret"}
#     return {"user_id": user_id, "user_info": ""}

# @app.get("/files/{file_path:path}") # there can't be space between `:` and other characters
# async def read_file(file_path: str):
#     return {"file_path": file_path}