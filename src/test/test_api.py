from fastapi.testclient import TestClient
from main import app
from src.python.commons.messages import Message

client = TestClient(app)


def test_get_country():
    response = client.get("/countries")
    assert response.status_code == 200


def test_get_cities():
    response = client.get("/cities/247")
    assert response.status_code == 200


def test_insert_country():
    response = client.post("/insert_country")
    assert response.status_code == 201
    assert response.json() == Message.found


def test_insert_state():
    response = client.post("/insert_state")
    assert response.status_code == 201


def test_insert_city():
    response = client.post("/insert_city")
    assert response.status_code == 201


def test_insert_person():
    data = {
        "first_name": "first_name",
        "last_name": "last_name",
        "middle_name": "middle_name",
        "date_of_birth": "2012-05-19 21:15:18",
        "gender_id": 1,
        "nationality": 347,
        "current_occupation": 1,
        "current_income": 1000000,
        "marital_status": 1,
        "num_children": 0,
        "education_level": 1,
        "email": "Julianne.OConner@kory.org",
        "phone": 14631234447
    }

    data_response = {
        "message": "success",
        "status_code": 201,
        "data": {
            "first_name": "first_name",
            "last_name": "last_name",
            "middle_name": "middle_name",
            "date_of_birth": "2012-05-19T21:15:18",
            "gender_id": 1,
            "nationality": 347,
            "current_occupation": 1,
            "current_income": 1000000,
            "marital_status": 1,
            "num_children": 0,
            "education_level": 1,
            "email": "Julianne.OConner@kory.org",
            "phone": 14631234447,
            "notes": None
        }
    }
    response = client.post("/insert_person/", json=data)
    assert response.status_code == 201
    assert response.json() == data_response


def test_get_person():
    data_response = {
        "message": "success",
        "status_code": 200,
        "data": {
            "id": 6,
            "first_name": "Kurtis",
            "last_name": "Elwyn.Skiles",
            "middle_name": "Weissnat",
            "date_of_birth": "2012-05-19T21:15:18",
            "gender_id": "Male",
            "nationality": "Uzbekistan",
            "current_occupation": "Artista",
            "current_income": 9260532.0,
            "marital_status": "Union Libre",
            "num_children": 1,
            "education_level": "Primaria",
            "email": "Telly.Hoeger@billy.biz",
            "phone": "210.067.6132",
            "notes": ""
        }
    }
    response = client.get("/get_person/6")
    assert response.status_code == 200
    assert response.json() == data_response


def test_delete_person():
    data_response = {
        "message": "success",
        "status_code": 200,
        "data": 6
    }
    response = client.put("/delete_person/6")
    assert response.status_code == 200
    assert response.json() == data_response


def test_update_person():
    send_data = data = {
        "first_name": "first_name",
        "last_name": "last_name",
        "middle_name": "middle_name",
        "date_of_birth": "2012-05-19 21:15:18",
        "gender_id": 1,
        "nationality": 347,
        "current_occupation": 1,
        "current_income": 1000000,
        "marital_status": 1,
        "num_children": 0,
        "education_level": 1,
        "email": "Julianne.OConner@kory.org",
        "phone": 14631234447
    }

    data_response = {
            "message": "success",
            "status_code": 200,
            "data": 7
        }

    response = client.put("/update_person/7", json=send_data)
    assert response.status_code == 200
    assert response.json() == data_response
