from src.python.db.database import Database
from src.python.db.execute_query import ExecuteQuery

from src.python.models.country import Country


class CountryQueries(Country):
    engine = Database.connection()

    @classmethod
    def get_all_countries(cls):
        """
        Get all countries from database.
        :return: list of countries.
        """
        query = 'SELECT * FROM technical_test.country'
        return ExecuteQuery.select(query)

    @classmethod
    def get_all_state(cls):
        """
        Get all states from database.
        :return: list of states.
        """
        query = 'SELECT * FROM technical_test.states'
        return ExecuteQuery.select(query)

    @classmethod
    def get_all_city(cls):
        """
        Get all cities from database.
        :return: list of states.
        """
        query = 'SELECT * FROM technical_test.city'
        return ExecuteQuery.select(query)

    @classmethod
    def get_city_by_name(cls, name):
        """
        Get all cities from database.
        :return: list of states.
        """
        query = "SELECT * FROM technical_test.city WHERE name = " + "'" + name + "'"
        return ExecuteQuery.select(query)
