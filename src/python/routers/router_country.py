from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import sessionmaker
from starlette.status import HTTP_200_OK, HTTP_201_CREATED

from src.python.commons.messages import Message
from src.python.commons.response import UJSONResponse
from src.python.db.database import Database
from src.python.services.cities import Cities
from src.python.services.countries import Countries
from src.python.services.create_data import CreateData

app_country = APIRouter()


@app_country.get("/countries")
def get_country():
    """
    Get all countries from database.
    :return: list of countries.
    """

    db = sessionmaker(bind=Database.connection())()
    result = Countries(db).get_countries()

    return UJSONResponse(
        Message.found,
        HTTP_200_OK,
        jsonable_encoder(result)
    )


@app_country.get("/cities/{country_id}")
def get_cities(country_id: int):
    """
    Get all cities from database with country_id
    :param country_id: id of country
    :return: list of cities.
    """

    db = sessionmaker(bind=Database.connection())()
    result = Cities(db).get_cities_by_country_id(country_id)

    return UJSONResponse(
        Message.found,
        HTTP_200_OK,
        jsonable_encoder(result)
    )


@app_country.post("/insert_country")
def insert_country():
    """
    Insert all countries from external api.
    :return: list of countries.
    """

    CreateData.insert_country()

    return UJSONResponse(
        Message.found,
        HTTP_201_CREATED
    )


@app_country.post("/insert_state")
def insert_state():
    """
    Insert all states from external api.
    :return: None.
    """

    CreateData.insert_state()

    return UJSONResponse(
        Message.found,
        HTTP_201_CREATED
    )


@app_country.post("/insert_city")
def insert_city():
    """
    Insert all cities from external api.
    :return: None.
    """

    CreateData.insert_city()

    return UJSONResponse(
        Message.found,
        HTTP_201_CREATED
    )
