from sqlalchemy import create_engine # сущность способная запускать БД
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Column, Integer, String
# Создаем движок базы данных
engine = create_engine("sqlite:///taskmanager.db", echo = True)

# Создаем локальную сессию
SessionLocal = sessionmaker(bind=engine)

# Создаем базовый класс
class Base(DeclarativeBase) :
    pass