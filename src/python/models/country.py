from src.python.db.database import Base
from sqlalchemy import Column, Integer, String


class Country(Base):

    __tablename__ = 'country'

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Colombia"
            }
        }
