import json
import logging

import random
from datetime import datetime
from sqlalchemy import text, TextClause

from src.python.commons.request_api import RequestApi
from src.python.db.execute_query import ExecuteQuery
from src.python.db.queries.country_queries import CountryQueries


class CreateData:
    __url: str = "https://www.universal-tutorial.com"
    __url_home: str = "https://api.clikalia.com/api/ReadPropertiesMySQL"
    __url_person: str = "https://jsonplaceholder.typicode.com/users"
    __headers: dict = {
        'Content-Type': 'application/json',
        'Cookie': 'cf_ob_info=504:7bb868546a398de8:MIA; cf_use_ob=443'
    }

    @classmethod
    def get_country(cls):
        """
        Get all countries from external api.
        :return: list of countries.
        """

        path: str = "/api/countries/"

        payload = json.dumps({
            'Authorization': 'nLsYM6PoE9D9ReXB_IvI-i2X-70ZauAITWgW4yiRAsEdcVsORc2awdoA5hPLroae94c eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7InVzZXJfZW1haWwiOiJtdmdhZGFnaUBnbWFpbC5jb20ifSwiZXhwIjoxNTY2MjM0ODU0fQ.nMWPN38zptwwDKAo11bFyjhCRuzNhZc6NqqCaYJVxP0',
            'Accept': 'application/json'
        })

        result = list(RequestApi.get(cls.__url + path, cls.__headers, payload))

        return result

    @classmethod
    def insert_country(cls):

        for i in cls.get_country():
            datos = {
                'name': i['country_name']
            }

            __query: TextClause = text("INSERT INTO country (name) VALUES (:name)")

            ExecuteQuery.insert(__query, datos)

    @classmethod
    def insert_state(cls):

        for i in CountryQueries.get_all_countries():

            country_id: int = i[0]
            state: str = i[1]
            path: str = "/api/states/" + state

            headers: dict = {
                'Content-Type': 'application/json',
                'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7InVzZXJfZW1haWwiOiJhc2tAdW5pdmVyc2FsLXR1dG9yaWFsLmNvbSIsImFwaV90b2tlbiI6IlQ2VlBOUmZXbkxFbmdsMHd2djctZ1d2Y09KRHFPSkptc3ZoNkNOdGo5a3p1Z1RSYkhvdXVET1NXeTdzYmJzdG5taDAifSwiZXhwIjoxNjgyMjc3NjUwfQ.LbUv_9fU5KxX3l0g1WZs4zg9GLU3-LbpvFf4UpXNui8',
                'Accept': 'application/json'
            }

            result = RequestApi.get(cls.__url + path, headers, None)

            for data in result:
                datos: dict = {
                    'name': data['state_name'],
                    'country_id': country_id
                }

                __query: TextClause = text("INSERT INTO states (name, country_id) VALUES (:name, :country_id)")

                ExecuteQuery.insert(__query, datos)

    @classmethod
    def insert_city(cls):

        for i in CountryQueries.get_all_state():

            state_id: int = i[0]
            city: str = i[1]
            path: str = "/api/cities/" + city

            headers: dict = {
                'Content-Type': 'application/json',
                'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7InVzZXJfZW1haWwiOiJhc2tAdW5pdmVyc2FsLXR1dG9yaWFsLmNvbSIsImFwaV90b2tlbiI6IlQ2VlBOUmZXbkxFbmdsMHd2djctZ1d2Y09KRHFPSkptc3ZoNkNOdGo5a3p1Z1RSYkhvdXVET1NXeTdzYmJzdG5taDAifSwiZXhwIjoxNjgyMjc3NjUwfQ.LbUv_9fU5KxX3l0g1WZs4zg9GLU3-LbpvFf4UpXNui8',
                'Accept': 'application/json'
            }

            result = RequestApi.get(cls.__url + path, headers, None)

            try:
                for data in result:
                    datos: dict = {
                        'name': data['city_name'],
                        'state_id': state_id
                    }

                    __query: TextClause = text("INSERT INTO city (name, state_id) VALUES (:name, :state_id)")

                    ExecuteQuery.insert(__query, datos)

            except TypeError as e:
                logging.error(e)

    @classmethod
    def insert_home(cls, number_of_items: int):

        data = {
            "numberOfItems": int(number_of_items),
            "country": "es",
            "province": "Madrid",
            "sort": {
                "name": "Más relevantes",
                "value": "destacados",
                "moreParamsEvaluate": True,
                "selected": True
            },
            "typeComercialization": "sale"
        }
        result = RequestApi.post(cls.__url_home, data)

        for r in result['result']:

            for i in CountryQueries.get_city_by_name(r['ciudad']):

                if i[2] == 5049:
                    address: str = str({
                        'distrito': r['distrito'],
                        'barrio': r['barrio'],
                        'calle': r['calle'],
                        'number': r['numero']
                    })

                    data: dict = {
                        'address': address,
                        'city_id': 5049,
                        'zip_code': r['codigo_postal'],
                        'num_bedrooms': r['habitaciones'],
                        'num_bathrooms': r['banos'],
                        'square_footage': r['metros'],
                        'year_built': r['fecha_construccion']
                    }

                    __query: TextClause = text('INSERT INTO home (address, city_id, zip_code, num_bedrooms, '
                                               'num_bathrooms, square_footage, year_built) VALUES (:address, '
                                               ':city_id, :zip_code, :num_bedrooms, :num_bathrooms, :square_footage, '
                                               ':year_built)')

                    ExecuteQuery.insert(__query, data)

    @classmethod
    def insert_person(cls):

        result = RequestApi.get(cls.__url_person, None, None)
        inicio = datetime(1990, 1, 30)
        final = datetime(2023, 5, 28)

        random_date = inicio + (final - inicio) * random.random()

        for data in result:
            first_name: str = data['name'].split(' ')[0]
            last_name: str = data['username']
            middle_name: str = data['name'].split(' ')[1]
            date_of_birth = random_date
            gender_id: int = random.randint(1, 3)
            nationality_id: int = random.randint(247, 491)
            current_occupation: int = random.randint(1, 22)
            current_income: int = random.randint(1000000, 9999999)
            marital_status_id: int = random.randint(1, 5)
            num_children: int = random.randint(0, 5)
            education_id: int = random.randint(1, 7)
            email: str = data['email']
            phone: str = data['phone']

            datos: dict = {
                'first_name': first_name,
                'last_name': last_name,
                'middle_name': middle_name,
                'date_of_birth': date_of_birth,
                'gender_id': gender_id,
                'nationality': nationality_id,
                'current_occupation': current_occupation,
                'current_income': current_income,
                'marital_status': marital_status_id,
                'num_children': num_children,
                'education_level': education_id,
                'email': email,
                'phone': phone,
                'notes': ''
            }

            __query: TextClause = text('CALL post_insert_person (:first_name, :last_name, :middle_name, '
                                       ':date_of_birth, :gender_id, :nationality, :current_occupation, '
                                       ':current_income, :marital_status, :num_children, :education_level, '
                                       ':email, :phone, :notes)')

            ExecuteQuery.insert(__query, datos)
