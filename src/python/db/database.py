from os import environ

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Database:

    @staticmethod
    def connection():
        """
            Create sql engine connection to mysql database.

            :return: engine to create connections and all sql queries.
            """
        # mysql_url = environ.get("ENV_URL_MYSQL")

        mysql_url = "mysql+mysqldb://root:Nemoujaja@localhost:3306/technical_test"

        if not mysql_url:
            raise EnvironmentError("ENV_URL_MYSQL environment variable must be set")
        try:
            return create_engine(mysql_url, echo=True)

        except Exception:
            raise RuntimeError("can not connect to database MYSQL")
