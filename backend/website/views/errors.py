from fastapi import HTTPException

from fastapi import APIRouter


website_errors = APIRouter(prefix="", include_in_schema=False)

items = {"foo": "The Foo Wrestlers"}


@website_errors.get("/items/{item_id}")
async def read_item(item_id: str):
    print("55522")
    if item_id not in items:
        print("werew666")
        raise HTTPException(
            status_code=502,
            detail="Item not found",
        )
    return {"item": items[item_id]}
