from sqlalchemy.orm import Session
import models, schemas
from datetime import datetime

def get_dispositivos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Dispositivo).offset(skip).limit(limit).all()

def create_dispositivo(db: Session, dispositivo: schemas.DispositivoCrear):
    db_dispositivo = models.Dispositivo(
        nombre=dispositivo.nombre, ip=dispositivo.ip,
        marca=dispositivo.marca, modelo=dispositivo.modelo
    )
    db.add(db_dispositivo)
    db.commit()
    db.refresh(db_dispositivo)
    return db_dispositivo

def get_eventos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.EventoSyslog).order_by(models.EventoSyslog.id.desc()).offset(skip).limit(limit).all()

def create_evento(db: Session, evento: schemas.EventoCrear):
    db_evento = models.EventoSyslog(
        dispositivo_id=evento.dispositivo_id,
        timestamp=datetime.utcnow().isoformat(),
        origen_ip=evento.origen_ip, severidad=evento.severidad,
        mensaje=evento.mensaje, es_sintetico=True
    )
    db.add(db_evento)
    db.commit()
    db.refresh(db_evento)
    return db_evento