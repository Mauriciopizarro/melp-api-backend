import os
from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()

if not os.getenv("DEBUG") or os.getenv("DEBUG").lower() == "true":
    load_dotenv("./.env.test")
else:
    load_dotenv("./.env")


class Settings(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str


settings = Settings()
