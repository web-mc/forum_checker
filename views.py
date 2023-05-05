import logging

from sanic.response import text


from app import app



# Главная
@app.get("/")
@app.ext.template("index.html")
async def main_page(request):
    sdfsf="sdfsfd"
    return {"seq": ["one111", "two"]}