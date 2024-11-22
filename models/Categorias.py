from typing import Optional
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String
from configs.db import Base


class CategoriaPy(BaseModel): 
    id: Optional[int] = Field(default=None)
    name: str


class CategoriasDB(Base):
    __tablename__ = 'categorias'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True)