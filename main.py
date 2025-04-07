from fastapi import FastAPI, HTTPException, Depends
from database import get_db
from sqlalchemy.orm import Session
import models
from typing import List
import pyd
app = FastAPI()

@app.get('/product', response_model=List[pyd.BaseProduct])
def get_all_products(db: Session=Depends(get_db)):
    products = db.query(models.Product).all()
    return products

@app.get('/product/{product_id}', response_model=pyd.BaseProduct)
def get_product_by_id(product_id: int, db: Session=Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    
    if not product:
        raise HTTPException(404, 'Товар не найден')
    return product

@app.post('/product', response_model=pyd.BaseProduct)
def create_product(product: pyd.CreateProduct, db: Session=Depends(get_db)):
    product_db = db.query(models.Product).filter(models.Product.name == product.name).first()
    if product_db:
        raise HTTPException(400, 'Уже существует')
    
    product_db = models.Product()
    product_db.name = product.name

    db.add(product_db)
    db.commit()

    return product_db

@app.delete('/product/{product_id}')
def delete_product(product_id: int, db: Session=Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(404, 'Товар не найден')
    db.delete(product)
    db.commit()
    return {'msg': 'Удалено'}

@app.get('/student', response_model=List[pyd.BaseStudent])
def get_all_students(db: Session=Depends(get_db)):
    students = db.query(models.Student).all()
    return students

@app.get('/student/{student_id}', response_model=pyd.BaseStudent)
def get_student_by_id(student_id: int, db: Session=Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    
    if not student:
        raise HTTPException(404, 'Студент не найден')
    return student

@app.post('/student', response_model=pyd.BaseStudent)
def create_student(student: pyd.CreateStudent, db: Session=Depends(get_db)):
    student_db = models.Student()

    student_db.surname = student.surname
    student_db.name = student.name
    student_db.group = student.group

    db.add(student_db)
    db.commit()

    return student_db

@app.delete('/student/{student_id}')
def delete_student(student_id: int, db: Session=Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        raise HTTPException(404, 'Товар не найден')
    db.delete(student)
    db.commit()
    return {'msg': 'Удалено'}