from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from starlette.status import HTTP_201_CREATED

from src.python.commons.messages import Message
from src.python.commons.response import UJSONResponse
from src.python.services.create_data import CreateData

app_home = APIRouter()


@app_home.post("/insert_home/{number_of_items}")
def insert_home(number_of_items: int):
    """
    Insert all cities from external api.
    :return: None.
    """

    CreateData.insert_home(number_of_items)

    return UJSONResponse(
        Message.found,
        HTTP_201_CREATED,
        jsonable_encoder('Inserted')
    )
