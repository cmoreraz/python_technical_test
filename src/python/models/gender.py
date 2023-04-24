from sqlalchemy import Column, Integer, String

from src.python.db.database import Base


class Gender(Base):
    __tablename__ = "gender"
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String)
