import schedule

from src.python.services.create_data import CreateData


schedule.every().sunday.at("15:39").do(CreateData.insert_home(1000))
