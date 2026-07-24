from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

URL_BASE_DATOS = "sqlite:///estudiantes_ebau.db"

engine = create_engine(URL_BASE_DATOS, connect_args={"check_same_thread": False}) # conectando python con sqlite

Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # ventanilla de sesión para interactuar con la base de datos

Base = declarative_base() # molde base para crear las tablas de la base de datos

# Funcion para que FastAPI abra y cierre sesion:
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()
