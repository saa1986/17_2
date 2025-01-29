from app.backend.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
   # user_id = Column(Integer, ForeignKey('tasks.id'))
    # Связь с задачами
    task = relationship('Task', back_populates='users')

# Вывод схемы таблицы после определения класса
print(CreateTable(User.__table__))