from pydantic import BaseModel
from sqlalchemy import Column, Integer, ForeignKey
from configs.db import Base


class CarritoPy(BaseModel): 
    id_article: int
    id_user: int
    cantidad: int


class CarritoDB(Base):
    __tablename__ = 'carrito'
    
    id_article = Column(Integer, ForeignKey('articulos.id'), primary_key=True)
    id_user = Column(Integer, ForeignKey('usuario.id'), primary_key=True)
    cantidad = Column(Integer)
