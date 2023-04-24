from src.python.db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from src.python.models.country import Country


class City(Base):
    __tablename__ = 'city'

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)
    country_id: Country = Column(Integer, ForeignKey('country.id'))


