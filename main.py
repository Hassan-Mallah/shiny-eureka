from fastapi import Security, Depends, FastAPI, HTTPException
from fastapi.security.api_key import APIKeyHeader, APIKey
from typing import Optional
from starlette.status import HTTP_403_FORBIDDEN
from starlette.responses import RedirectResponse, JSONResponse

app = FastAPI()

API_KEY = "1234567asdfgh"
API_KEY_NAME = "access_token"

api_key_header = APIKeyHeader(name=API_KEY_NAME)


async def get_api_key(
        api_key_header: str = Security(api_key_header),
):
    if api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )


@app.post("/auth/")
async def read_items(api_key: APIKey = Depends(get_api_key)):
    return {"token": 'token'}


@app.get("/")
async def read_root():
    return {"Hello": "World", "status": "venv installed"}


# e.g. http://127.0.0.1:8000/items/5?q=This%20is%205
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
