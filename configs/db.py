from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Ruta de la base de datos
DATABASE_URL =  'sqlite:///shop.db'

# Creamos el motor, al comienzo de la ruta de la BD ya especifica que es SQLite
engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})

# Luego creamos los parámetros para las sesiones que se crean de dicho motor
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Creamos el mapeado ORM
Base = declarative_base()

# Creamos la función para el uso de la sesión
def get_db() :
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()