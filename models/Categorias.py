from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from configs.db import Base


class CategoriaPy(BaseModel): 
    id: int
    name: str


class CategoriasDB(Base):
    __tablename__ = 'categorias'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)