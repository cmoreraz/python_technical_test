from fastapi import FastAPI

from src.python.middlewares.error_handler import ErrorHandler
from src.python.routers.router_country import app_country
from src.python.routers.router_home import app_home
from src.python.routers.router_person import app_person

app = FastAPI()

app.title = "Technical Test"
app.version = "0.0.1"

app.include_router(app_person)
app.include_router(app_country)
app.include_router(app_home)

app.add_middleware(ErrorHandler)

