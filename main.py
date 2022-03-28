from fastapi import Depends, FastAPI
from fastapi.security.api_key import APIKey
from typing import Optional
from token_key import get_api_key

app = FastAPI()


@app.post("/auth/")
async def read_items(api_key: APIKey = Depends(get_api_key)):
    return {"token": 'token is correct :)'}


@app.get("/")
async def read_root():
    return {"Hello": "World", "status": "venv installed"}


# e.g. http://127.0.0.1:8000/items/5?q=This%20is%205
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
