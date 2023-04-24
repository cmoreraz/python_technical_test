from datetime import datetime
from pydantic import BaseModel


class Person(BaseModel):

    first_name: str
    last_name: str
    middle_name: str
    date_of_birth: datetime
    gender_id: int
    nationality: int
    current_occupation: int
    current_income: int
    marital_status: int
    num_children: int
    education_level: int
    email: str
    phone: int
    notes: str | None = None
