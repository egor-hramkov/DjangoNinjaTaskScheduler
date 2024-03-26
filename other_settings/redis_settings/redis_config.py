import os

from dotenv import load_dotenv

load_dotenv()

REDIS_CONFIG = {
    "REDIS_HOST": os.environ.get("REDIS_HOST"),
}
