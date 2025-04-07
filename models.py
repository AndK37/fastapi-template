from database import Base
from sqlalchemy import Column, Integer, String

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    surname = Column(String(255))
    name = Column(String(255))
    group = Column(String(255))