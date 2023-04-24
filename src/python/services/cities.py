from src.python.models.city import City


class Cities(City):

    def __init__(self, db) -> None:
        self.db = db

    def get_cities_by_country_id(self, country_id: int):
        """
        Get all cities from database with country_id
        :param country_id: id of country
        :return: list of cities.
        """
        result = self.db.query(City).filter(City.country_id == country_id).all()

        return result

    def post_city(self, city: City):
        """
        Post city to database
        :param city: city
        :return: city
        """
        self.db.add(city)
        self.db.commit()
        return city
