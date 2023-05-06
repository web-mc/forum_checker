from app import app
import uvicorn
from views import  main, errors


if __name__ == "__main__":
    uvicorn.run("site_runner:app", port=5000, reload=True)
