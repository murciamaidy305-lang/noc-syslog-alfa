# Herramientas de SQLAlchemy para conectar con la base de datos
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Le decimos que cree un archivo llamado 'noc_inteligente.db'
SQLALCHEMY_DATABASE_URL = "sqlite:///./noc_inteligente.db"

# 'engine' es el motor que hace funcionar la base de datos
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False} # Necesario para SQLite en FastAPI
)

# 'SessionLocal' será nuestra "ventana" temporal para leer o guardar datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 'Base' es la clase maestra de la que heredarán todos nuestros modelos
Base = declarative_base()
