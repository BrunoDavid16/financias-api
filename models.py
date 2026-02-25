from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.orm import DeclarativeBase
from pydantic import BaseModel
from typing import Optional

class Base(DeclarativeBase):
    pass

class Usuario(BaseModel):
    email: str
    senha: str

class UsuarioModel(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True)
    senha_hash = Column(String)

class Receita(BaseModel):
    valor: float
    descricao: str
    categoria: Optional[str]
    data: str

class ReceitaModel(Base):
    __tablename__ = "receita"
    id = Column(Integer, primary_key=True, autoincrement=True)
    valor = Column(Float)
    descricao = Column(String)
    categoria = Column(String)
    data = Column(String)

class Despesa(BaseModel):
    valor: float
    descricao: str
    categoria: Optional[str]
    data: str

class DespesaModel(Base):
    __tablename__ = "despesas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    valor = Column(Float)
    descricao = Column(String)
    categoria = Column(String)
    data = Column(String)