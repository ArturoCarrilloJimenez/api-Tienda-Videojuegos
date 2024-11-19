from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, Boolean
from configs.db import Base
from typing import Optional

class UsuarioPy(BaseModel): 
    id: int
    username: str
    password: Optional[str] = Field(default=None)
    name: Optional[str] = Field(default=None)
    admin: bool


class UsuarioDB(Base):
    __tablename__ = 'usuario'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True)
    password = Column(String(128))
    name = Column(String(100))
    email = Column(String(100))
    admin = Column(Boolean, default=False)