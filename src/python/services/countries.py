from src.python.models.country import Country


class Countries(Country):

    def __init__(self, db) -> None:
        self.db = db

    def get_countries(self):
        """
        Get all countries from database.
        :return: list of countries.
        """
        result = self.db.query(Country).all()

        return result
