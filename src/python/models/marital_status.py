from sqlalchemy import Column, Integer, String

from src.python.db.database import Base


class MaritalStatus(Base):
    __tablename__ = "marital_status"
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String)
