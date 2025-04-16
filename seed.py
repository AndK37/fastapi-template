from sqlalchemy.orm import Session
from database import engine
import models

models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)

with Session(bind=engine) as session:
    c1 = models.Category(name='Food')
    p1 = models.Product(name='Milk', category_id=1)
    s1 = models.Student(surname='Иванов', name='Иван', group='123456')
    session.add(c1)
    session.add(p1)
    session.add(s1)
    session.commit()