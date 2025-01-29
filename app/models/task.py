from app.backend.db import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable


class Task(Base):
    __tablename__ = 'tasks'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    slug = Column(String, unique=True, index=True)
#    user_id = Column(Integer, ForeignKey('users.id'))
    # Связь с пользователем
    user = relationship('User', back_populates='task')


# Печатаем SQL-запрос на создание таблицы после определения класса
print(CreateTable(Task.__table__))

