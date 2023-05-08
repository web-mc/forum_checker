from fastapi import HTTPException

from fastapi import APIRouter


website_errors = APIRouter(prefix="")


items = {"foo": "The Foo Wrestlers"}


@website_errors.get("/items/{item_id}", include_in_schema=False)
async def read_item(item_id: str):
    print("555")
    if item_id not in items:
        print("werew666")
        raise HTTPException(
            status_code=502,
            detail="Item not found",
        )
    return {"item": items[item_id]}
