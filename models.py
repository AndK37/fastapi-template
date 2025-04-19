from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Category(Base): # 1
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True)

class Product(Base): # N
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True)
    category_id = Column(Integer, ForeignKey('categories.id'))

    category = relationship("Category", backref='products')

    def __repr__(self):
        return f"<Products(id={self.id}, name={self.name}, category_id={self.category_id})>"

# class Student(Base):
#     __tablename__ = 'students'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     surname = Column(String(255))
#     name = Column(String(255))
#     group = Column(String(255))