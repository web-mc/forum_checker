import uvicorn

import config
from app import app


if __name__ == "__main__":
    uvicorn.run(
        "site_runner:app", host=config.SITE_HOST, port=config.SITE_PORT, reload=config.SITE_RELOAD
    )
