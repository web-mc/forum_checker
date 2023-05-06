from fastapi import HTTPException
from app import app


items = {"foo": "The Foo Wrestlers"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        print('werew666')
        raise HTTPException(status_code=502, detail="Item not found")
    return {"item": items[item_id]}