from typing import Optional
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from configs.db import Base


class ArticulosPy(BaseModel): 
    id: Optional[int] = Field(default=None)
    name: str
    price: int
    tax: float
    description: str
    image: str
    stock: int
    idCategory: int


class ArticulosDB(Base):
    __tablename__ = 'articulos'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True)
    price = Column(Float, default=0)
    tax = Column(Integer, default=0)
    description = Column(String(255))
    image = Column(String(255))
    stock = Column(Integer, default=0)
    idCategory = Column(Integer, ForeignKey('categorias.id'))
    def final_price(self):
        return self.price + (self.price * self.tax / 100)