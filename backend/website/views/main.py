from fastapi import APIRouter


website = APIRouter(prefix="", include_in_schema=False)


@website.get("/")
async def main_page():
    return {"message": "Hello5555 World"}
