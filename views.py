import logging


from app import app



# Главная GET
@app.get("/")
@app.ext.template("index.html")
async def main_page(request):
    sdfsf="sdfsfd555"
    return {"title": "Find forum"}