from app import app



@app.get("/")
async def main_page():
    return {"message": "Hello55 World"}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}


