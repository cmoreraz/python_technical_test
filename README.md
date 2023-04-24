# Python technical test

## Introduction

This is a technical test for Python developers. It is designed to test your ability to write clean, maintainable code and to demonstrate your understanding of Python.

## Instructions

### Prerequisites
- Python 3.11.2

### Installation
1. Create and activate virtual environment
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install requirements
   ```sh
   pip install -r requirements.txt
   ```
3. Execute the following command to run the application
   ```sh
   uvicorn main:app --reload
   ```
4. Execute tests
   ```sh
   pytest
   ```
   
## Tecnologies used
Durante la construcción de este proyecto, creamos una aplicación mediante una arquitectura REST, como framework usaremos:
- FastAPI 0.95.1
- schedule

Para la conexión a la base de datos, usaremos:
- SQLAlchemy 2.0.9
- MySQLClient 2.1.1

Para la documentación de la API, usaremos:
- Swagger 0.1.0

## SQL Database
### Installation

Se debe instalar MySQL en el equipo donde se ejecutara la aplicación, para ello se puede descargar desde el siguiente enlace: [MySQL](https://dev.mysql.com/downloads/mysql/), en este caso se utilizo la version 8.0.19.
Donde se debe crear una base de datos llamada `technical_test` y un usuario con los siguientes datos:
- user: `root`
- password: `Nemoujaja`

### Database model
De acuerdo al modelo de datos suministrado, se recomienda incluir mas tablas con el fin de normalizar la DB para poder evitar la duplicidad de informacion, por ejemplo:
-  En la tabla `person` se incluye el campo `nationality` como `FK` de la tabla `country`, para poder saber que personas son de que pais y evitar que en el front esto sea un campo libre, pero tambien se puede crear una tabla `nationality` y hacer la relación con la tabla `person` y `country`.
- En la tabla `person` se incluye el campo `current_occupation` como `FK` de la tabla `occupation`, para saber cual es la ocupacion de cada usuario.
- En la tabla `person` se incluye el campo `marital_status` como `FK` de la tabla `marital_status`, para saber el estado civil de cada usuario.
- En la tabla `person` se incluye el campo `education_level` como `FK` de la tabla `education_level`, para saber el nivel de educacion de cada usuario. 

En la solucion planteada se inluyeron nuevas tablas y relaciones entre las mismas, en vista de lo anterior, la base de datos quedo normalizada de la siguiente manera:

![](./readmi/sql_model.png)

A continuación se muestra el script de la base de datos:

```sql
-- Create database
create database technical_test;

-- Use database
use technical_test;

-- Create tables
create table country (
  id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  name varchar(50) UNIQUE NOT NULL
);

create table states (
    id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name varchar(100) UNIQUE NOT NULL,
    country_id int(11) NOT NULL, 
    CONSTRAINT city_ibhik_1 FOREIGN KEY (country_id) REFERENCES country (id)
);

create table city (
  id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  name varchar(50) UNIQUE NOT NULL,
  state_id int(11) NOT NULL,
  KEY state_id (state_id),
  CONSTRAINT city_ibfk_1 FOREIGN KEY (state_id) REFERENCES states (id)
);

create table gender (
  id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  name varchar(20) UNIQUE NOT NULL
);

create table home (
  id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  address varchar(200) NOT NULL,
  city_id int(11) NOT NULL,
  zip_code varchar(20) NOT NULL,
  num_bedrooms int(11) NOT NULL,
  num_bathrooms int(11) NOT NULL,
  square_footage int(11) NOT NULL,
  year_built int(11) NOT NULL,
  KEY city_id (city_id),
  CONSTRAINT home_ibfk_1 FOREIGN KEY (city_id) REFERENCES city (id)
);

create table social_media_network (
  id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name varchar(50) NOT NULL,
  url varchar(200) NOT NULL
);

create table relationship_type (
  id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name varchar(20) NOT NULL
);

create table occupation (
    id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name varchar(100) NOT NULL
);

create table occupation_type (
    id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name varchar(100) NOT NULL
);

create table marital_status (
    id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name varchar(100) NOT NULL
);

create table education_level (
    id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name varchar(100) NOT NULL
);

create table person (
    id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name varchar(50) NOT NULL,
    last_name varchar(100) NOT NULL,
    middle_name varchar(50) NOT NULL,
    date_of_birth datetime not null,
    gender_id int(11) NOT NULL,
    nationality int(11),
    current_occupation int(11),
    current_income decimal(10,2) NOT NULL,
    marital_status int(11),
    num_children int NOT NULL,
    education_level int(11),
    email varchar(100) NOT NULL,
    phone varchar(20) NOT NULL,
    notes text NOT NULL,
    KEY education_level (education_level),
    CONSTRAINT person_ifk_5 FOREIGN KEY (education_level) REFERENCES education_level (id),
    KEY marital_status_id (marital_status),
    CONSTRAINT person_ifk_4 FOREIGN KEY (marital_status) REFERENCES marital_status (id),
    KEY occupation_id (current_occupation),
    CONSTRAINT person_ifk_1 FOREIGN KEY (current_occupation) REFERENCES occupation (id),
    KEY country_id (nationality),
    CONSTRAINT person_ifk_2 FOREIGN KEY (nationality) REFERENCES country (id),
    KEY gender_id (gender_id),
    CONSTRAINT person_ifl_3 FOREIGN KEY (gender_id) REFERENCES gender (id)
);

create table social_media_account (
    id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    person_id int(11) NOT NULL,
    network_id int(11) NOT NULL,
    account_url varchar(255) NOT NULL,
    KEY person_id (person_id),
    CONSTRAINT social_media_account_ifk_1 FOREIGN KEY (person_id) REFERENCES person (id),
    KEY social_media_network_id (network_id),
    CONSTRAINT social_media_account_ifk_2 FOREIGN KEY (network_id) REFERENCES social_media_network (id)
);

create table family_relationship(
    id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    person_id int(11) NOT NULL,
    relationship_type_id int(11) NOT NULL,
    relative_id int(11) NOT NULL,
    KEY person_id (person_id),
    CONSTRAINT family_relationship_ifk_1 FOREIGN KEY (person_id) REFERENCES person (id),
    KEY relationship_type_id (relationship_type_id),
    CONSTRAINT family_relationship_ifk_2 FOREIGN KEY (relationship_type_id) REFERENCES relationship_type (id),
    KEY related_person_id (relative_id),
    CONSTRAINT family_relationship_ifk_3 FOREIGN KEY (relative_id) REFERENCES person (id)
);

create table location_history (
    id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    person_id int(11) NOT NULL,
    visit_date datetime NOT NULL,
    location point NOT NULL,
    place_name varchar(255) NOT NULL,
    source_type_id int(11) NOT NULL,
    KEY person_id (person_id),
    CONSTRAINT location_history_ifk_1 FOREIGN KEY (person_id) REFERENCES person (id),
    KEY source_type_id (source_type_id),
    CONSTRAINT location_history_ifk_2 FOREIGN KEY (source_type_id) REFERENCES source_type (id)
);

create table source_type (
    id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name varchar(100) UNIQUE NOT NULL
);

-- Insert data into tables
insert into gender (name)
values ('Male'), ('Female'), ('Other');
```

Esta base de datos permite almacenar información de personas, sus relaciones familiares, sus cuentas de redes sociales, sus propiedades (casa) y la ubicación, entre otros.

## Structure of the project
```bash
├── README.md
├── requirements.txt
├── src
│   ├── python
│   │   ├── __init__.py
│   │   │   ├── commons
│   │   │   │   ├── __init__.py
│   │   │   │   ├── messages.py
│   │   │   │   ├── request_api.py
│   │   │   │   ├── response.py
│   │   │   ├── controller
│   │   │   │   ├── __init__.py
│   │   │   │   ├── api.py
│   │   │   ├── db
│   │   │   │   ├── database.py
│   │   │   │   ├── execute_query.py
│   │   │   │   ├── __init__.py
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── country_queries.py
│   │   │   ├── middlewares
│   │   │   │   ├── __init__.py
│   │   │   │   ├── error_handler.py
│   │   │   ├── models
│   │   │   │   ├── __init__.py
│   │   │   │   ├── city.py
│   │   │   │   ├── country.py
│   │   │   │   ├── education_level.py
│   │   │   │   ├── gender.py
│   │   │   │   ├── marital_status.py
│   │   │   │   ├── occupation.py
│   │   │   │   ├── person.py
│   │   │   ├── routers
│   │   │   │   ├── __init__.py
│   │   │   │   ├── router_country.py
│   │   │   │   ├── router_home.py
│   │   │   │   ├── router_person.py
│   │   │   ├── schedule
│   │   │   │   ├── __init__.py
│   │   │   │   ├── create_home.py
│   │   │   ├── services
│   │   │   │   ├── __init__.py
│   │   │   │   ├── cities.py
│   │   │   │   ├── countries.py
│   │   │   │   ├── create_data.py
│   │   │   │   ├── person_controller.py
│   ├── test
│   │   ├── __init__.py
│   │   │   ├── test_api.py
```

![](./readmi/proyecto.png)

## Cron Job 
Con el fin de insertar datos aleatorios para las siguientes tablas:
- country
- states
- city
- home
- person


Para esto se creó un cron job que se ejecuta en el dia y la hora configurada, el cual llama a una API que inserta datos aleatorios en las tablas mencionadas anteriormente.
- Para ello se utilizó la librería schedule, la cual permite ejecutar un método en un tiempo determinado, en este caso se ejecuta el método insert_home() de la clase CreateData, el cual inserta datos aleatorios en la tabla home, en el dia y hora configurada.
```python
import schedule

from src.python.services.create_data import CreateData

schedule.every().sunday.at("15:39").do(CreateData.insert_home(1000))
```
Tambien se crearon varias API´s, que insertan datos aleatorios en las tablas mencionadas anteriormente, estas son:
- insert_country
- insert_state
- insert_city
- insert_home
- insert_person

Para llenar las tablas relacionadas con los paises, se consumen los siguientes servicios:
```http request
GET /api/countries
GET /api/states/{country_name}
GET /api/cities/{state_name}

HTTP/1.1
Host: https://www.universal-tutorial.com
```
Y se debe enviar el siguiente body:
```json
{
    "Authorization": "nLsYM6PoE9D9ReXB_IvI-i2X-70ZauAITWgW4yiRAsEdcVsORc2awdoA5hPLroae94c eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7InVzZXJfZW1haWwiOiJtdmdhZGFnaUBnbWFpbC5jb20ifSwiZXhwIjoxNTY2MjM0ODU0fQ.nMWPN38zptwwDKAo11bFyjhCRuzNhZc6NqqCaYJVxP0",
    "Accept": "application/json"
}
```

Para llenar la tabla home, se consume el siguiente servicio:
```http request
POST /api/ReadPropertiesMySQL
HTTP/1.1
Host: https://api.clikalia.com
```
Y se debe enviar el siguiente body:
```json
{
    "numberOfItems": 1,
    "country": "es",
    "province": "Madrid",
    "sort": {
        "name": "Más relevantes",
        "value": "destacados",
        "moreParamsEvaluate": true,
        "selected": true
    },
    "typeComercialization": "sale"
}
```

Para diligenciar la tabla person, se consume el siguiente servicio:
```http request
POST /users
HTTP/1.1
Host: https://jsonplaceholder.typicode.com
```

## API´s
Para insertar datos en la tabla person, se debe consumir el siguiente servicio:
```http request
POST /get_person/{person_id}
HTTP/1.1
Host: http://localhost:8000
```
Para listar los datos del usuario se creo un store procedure 
```sql
CREATE PROCEDURE `get_select_person`(IN g_id int)
    BEGIN
        SELECT p.id, p.first_name, p.last_name, p.middle_name, p.date_of_birth, g.name, c.name,
               o.name, p.current_income, m.name, p.num_children, e.name, p.email, p.phone, p.notes FROM person p
            INNER JOIN gender g ON p.gender_id = g.id
            INNER JOIN country c on p.nationality = c.id
            INNER JOIN occupation o on p.current_occupation = o.id
            INNER JOIN marital_status m on p.marital_status = m.id
            INNER JOIN education_level e on p.education_level = e.id
                   WHERE p.id = g_id;
    END;
```
Este procedimeinto se llama en el back end de la siguiente manera:

```sql
CALL get_select_person(person_id);
```
- Response
```json
{
    "message": "success",
    "status_code": 200,
    "data": {
        "id": 5,
        "first_name": "first_name",
        "last_name": "last_name",
        "middle_name": "middle_name",
        "date_of_birth": "2012-05-19T21:15:18",
        "gender_id": "Male",
        "nationality": "Iran",
        "current_occupation": "Software Engineer",
        "current_income": 1000000.0,
        "marital_status": "Soltero",
        "num_children": 0,
        "education_level": "Primaria",
        "email": "Julianne.OConner@kory.org",
        "phone": "14631234447",
        "notes": null
    }
}
```


Para insertar datos en la tabla person, se debe consumir el siguiente servicio:
```http request
POST /insert_person
HTTP/1.1
Host: http://localhost:8000
```
Para insertar los datos del usuario se creo un store procedure 
```sql
CREATE PROCEDURE `post_insert_person`(IN i_first_name varchar(50), IN i_last_name varchar(100), IN
    i_middle_name varchar(50), IN i_date_of_birth datetime, IN i_gender_id int, IN
    i_nationality int, IN i_current_occupation int, IN i_current_income decimal(10,2), IN
    i_marital_status int, IN i_num_children int, IN i_education_level int, IN i_email varchar(100), IN
    i_phone varchar(20), IN i_notes text)
    BEGIN
        INSERT INTO person (first_name, last_name, middle_name, date_of_birth,
                            gender_id, nationality, current_occupation, current_income,
                            marital_status, num_children, education_level, email, phone, notes)
            values
                (i_first_name, i_last_name, i_middle_name, i_date_of_birth, i_gender_id, i_nationality,
                 i_current_occupation, i_current_income, i_marital_status, i_num_children,
                 i_education_level, i_email, i_phone, i_notes);
    END;

```
Este procedimeinto se llama en el back end de la siguiente manera:
```sql
CALL post_insert_person(first_name, last_name, middle_name, date_of_birth,
                            gender_id, nationality, current_occupation, current_income,
                            marital_status, num_children, education_level, email, phone, notes);
```

- Response

```json
{
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
        "notes": null
    }
}
```

Para actualizar datos en la tabla person, se debe consumir el siguiente servicio:
```http request
POST /update_person/{person_id}
HTTP/1.1
Host: http://localhost:8000
```
Para insertar los datos del usuario se creo un store procedure 
```sql
CREATE PROCEDURE `put_update_person`(IN u_id int, IN u_first_name varchar(50), IN u_last_name varchar(100), IN
    u_middle_name varchar(50), IN u_date_of_birth datetime, IN u_gender_id int, IN
    u_nationality int, IN u_current_occupation int, IN u_current_income decimal(10,2), IN
    u_marital_status int, IN u_num_children int, IN u_education_level int, IN u_email varchar(100), IN
    u_phone varchar(20), IN u_notes text)
    BEGIN
        UPDATE person SET first_name=u_first_name, last_name=u_last_name, middle_name=u_middle_name, date_of_birth=u_date_of_birth,
                            gender_id=u_gender_id, nationality=u_nationality, current_occupation=u_current_occupation,
                            current_income=u_current_income, marital_status=u_marital_status, num_children=u_num_children,
                            education_level=u_education_level, email=u_email, phone=u_phone, notes=u_notes
            WHERE id = u_id;
    END;

```
Este procedimeinto se llama en el back end de la siguiente manera:
```sql
CALL put_update_person (id, first_name, last_name, middle_name, date_of_birth, gender_id, nationality, current_occupation, 
                        current_income, marital_status, num_children, education_level, email, phone, notes);
```

- Response

```json
{
    "message": "success",
    "status_code": 200,
    "data": 4
}
```

Para eliminar datos en la tabla person, se debe consumir el siguiente servicio:
```http request
POST /delete_person/{person_id}
HTTP/1.1
Host: http://localhost:8000
```
Para insertar los datos del usuario se creo un store procedure 
```sql
CREATE PROCEDURE `put_delete_person`(IN d_id int)
    BEGIN
        DELETE FROM person WHERE id = d_id;
    END;
```
Este procedimeinto se llama en el back end de la siguiente manera:
```sql
CALL put_delete_person(d_id);
```

- Response

```json
{
    "message": "success",
    "status_code": 200,
    "data": 4
}
```
