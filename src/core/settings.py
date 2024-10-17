import pathlib
import dotenv
import os


class Settings:
    def __init__(self):
        dotenv.load_dotenv(dotenv.find_dotenv())
        self._db_host = os.getenv('DB_HOST')
        self._db_user = os.getenv('DB_USER')
        self._db_password = os.getenv('DB_PASSWORD')
        self._db_name = os.getenv('DB_NAME')

    def get_db_host(self):
        return self._db_host

    def get_db_user(self):
        return self._db_user

    def get_db_password(self):
        return self._db_password

    def get_db_name(self):
        return self._db_name

settings = Settings()