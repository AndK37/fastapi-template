from pydantic import BaseModel, Field

class CreateProduct(BaseModel):
    name: str = Field(min_length=3, max_length=255, example='Milk')

class CreateStudent(BaseModel):
    id: int = Field(example=1)
    surname: str = Field(min_length=1, max_length=32, example='Иванов')
    name: str = Field(min_length=1, max_length=32, example='Иван')
    group: str = Field(min_length=6, max_length=6, example='123456')