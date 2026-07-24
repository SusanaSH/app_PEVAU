from sqlalchemy import Column, Integer, String
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios" #Nombre de la tabla

    id = Column(Integer, primery_key=True, index=True) #Columna id, clave primaria
    nombre=(Column(String, index=True)) #Columna nombre, tipo String
    email=Column(String, unique=True, index=True) #Columna email, tipo String, unico
    password=Column(String)