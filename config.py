from os import getenv

from dotenv import load_dotenv

load_dotenv()


SITE_HOST = getenv("SITE_HOST")
SITE_PORT = int(getenv("SITE_PORT"))