from pydantic import BaseModel, Field

class BaseProduct(BaseModel):
    id: int = Field(example=1)
    name: str = Field(example='Milk')

class BaseStudent(BaseModel):
    id: int = Field(example=1)
    surname: str = Field(example='Иванов')
    name: str = Field(example='Иван')
    group: str = Field(example='123456')