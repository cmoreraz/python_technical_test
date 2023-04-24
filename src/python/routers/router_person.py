from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from starlette.status import HTTP_200_OK, HTTP_201_CREATED

from src.python.commons.messages import Message
from src.python.commons.response import UJSONResponse
from src.python.models.person import Person
from src.python.services.person_controller import PersonController

app_person = APIRouter()


@app_person.get("/get_person/{person_id}")
def get_person(person_id: int):
    """
    Get person from database.
    :return: JSON.
    """

    result = PersonController.get_person_by_id(person_id)

    data = {
        'id': result[0][0],
        'first_name': result[0][1],
        'last_name': result[0][2],
        'middle_name': result[0][3],
        'date_of_birth': result[0][4],
        'gender_id': result[0][5],
        'nationality': result[0][6],
        'current_occupation': result[0][7],
        'current_income': result[0][8],
        'marital_status': result[0][9],
        'num_children': result[0][10],
        'education_level': result[0][11],
        'email': result[0][12],
        'phone': result[0][13],
        'notes': result[0][14],
    }

    print(data)
    return UJSONResponse(
        Message.found,
        HTTP_200_OK,
        jsonable_encoder(data)
    )


@app_person.post("/insert_person/")
def insert_person(person: Person):
    """
    Insert person to database.
    :return: JSON.
    """

    PersonController.insert_person(person)

    return UJSONResponse(
        Message.found,
        HTTP_201_CREATED,
        jsonable_encoder(person)
    )


@app_person.put("/update_person/{person_id}")
def update_person(person_id: int, person: Person):
    """
    Update person to database.
    :return: JSON.
    """

    PersonController.update_person(person_id, person)

    return UJSONResponse(
        Message.found,
        HTTP_200_OK,
        jsonable_encoder(person_id)
    )


@app_person.put("/delete_person/{person_id}")
def delete_person(person_id: int):
    """
    Delete person from database.
    :param person_id:
    :return:
    """

    PersonController.delete_person(person_id)

    return UJSONResponse(
        Message.found,
        HTTP_200_OK,
        jsonable_encoder(person_id)
    )
