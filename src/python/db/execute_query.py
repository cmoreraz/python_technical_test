from src.python.db.database import Database
from sqlalchemy import text
import logging


class ExecuteQuery:
    engine = Database.connection()

    @classmethod
    def select(cls, query):
        with cls.engine.connect() as connection:
            result = connection.execute(text(query)).fetchall()
        return result

    @classmethod
    def insert(cls, query, data):
        """
        Insert data in database.
        :param query: query to execute.
        :param data: data to insert.
        :return: None.
        """

        try:
            with cls.engine.connect() as connection:
                connection.execute(query, data)
                connection.commit()

        except Exception as e:
            logging.error(e)
