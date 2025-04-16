from .base_models import *
from typing import List


class CategorySchema(BaseCategory):
    products: List[BaseProduct]


class ProductSchema(BaseProduct):
    categories: List[BaseCategory]