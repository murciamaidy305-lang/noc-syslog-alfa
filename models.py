# Importamos los tipos de datos de SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from database import Base
from datetime import datetime

# TABLA 1: Inventario de Dispositivos
class Dispositivo(Base):
    __tablename__ = "dispositivos" # Nombre de la tabla en la base de datos

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    ip = Column(String, unique=True, index=True) # La IP no se puede repetir
    marca = Column(String) # Cisco, Fortinet, Huawei
    modelo = Column(String)
    estado = Column(String, default="Activo")
    fecha_actualizacion = Column(DateTime, default=datetime.utcnow)

# TABLA 2: Logs (Eventos Syslog)
class EventoSyslog(Base):
    __tablename__ = "eventos_syslog"

    id = Column(Integer, primary_key=True, index=True)
    dispositivo_id = Column(Integer, ForeignKey("dispositivos.id")) # Relaciona el log con el equipo
    timestamp = Column(String)
    origen_ip = Column(String)
    severidad = Column(Integer) # Del 0 al 7
    mensaje = Column(String)
    es_sintetico = Column(Boolean, default=True) # Para saber si es de prueba