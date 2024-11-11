from dotenv import load_dotenv #импортируем объект
import os #импортируем файл

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session,DeclarativeBase

load_dotenv() #подгружает .env



DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL, echo=True) #создание движка на котором будет все работать

session_factory = sessionmaker(bind=engine) #сессия это любое подключение к бж, а именно это контроллер сессий(фабрика сессий)

class Base(DeclarativeBase):    #базовый класс бд, от него дальше будут создаваться модели. Модель - схема таблицы
    pass


