from sqlalchemy import Column, Integer, String

from src.python.db.database import Base


class Occupation(Base):
    __tablename__ = 'occupation'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String)
