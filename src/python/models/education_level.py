from sqlalchemy import Column, Integer, String

from src.python.db.database import Base


class EducationLevel(Base):
    __tablename__ = "education_level"
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String)
