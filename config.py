from os import getenv

from dotenv import load_dotenv


load_dotenv()

SITE_HOST = str(getenv("SITE_HOST", "127.0.0.1"))
SITE_PORT = int(getenv("SITE_PORT", "5000"))
SITE_RELOAD = bool(getenv("SITE_RELOAD", "0"))
