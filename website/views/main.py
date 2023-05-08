from fastapi import APIRouter


website = APIRouter(prefix="")


@website.get("/", include_in_schema=False)
async def main_page():
    return {"message": "Hello5555 World"}
