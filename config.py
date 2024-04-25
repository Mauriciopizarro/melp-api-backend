import os
from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()

if not os.getenv("DEBUG") or os.getenv("DEBUG").lower() == "true":
    load_dotenv("./.env.test")
else:
    load_dotenv("./.env")


class Settings(BaseSettings):
    MYSQL_URL: str


settings = Settings()
