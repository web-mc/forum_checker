from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.utils import get_openapi

# Импортируем блупринты
from backend.website.views.main import website
from backend.website.views.errors import website_errors


app = FastAPI(docs_url=None)

# Папка со стаиикой
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

# Подключаем блупринты
app.include_router(website)
app.include_router(website_errors)


# Свои настройки API доков
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Forum Chacker API",
        version="1.0",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
