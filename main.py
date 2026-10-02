from fastapi import FastAPI, Depends, Request, HTTPException
from fastapi.responses import PlainTextResponse
from sqlalchemy.orm import Session
from typing import List
from fastapi.templating import Jinja2Templates

from database import engine, SessionLocal
import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="NOC Syslog Inteligente", version="0.1.0")
templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def leer_raiz():
    return {"mensaje": "API del NOC Inteligente corriendo", "estado": "Alfa"}

@app.post("/dispositivos/", response_model=schemas.DispositivoRespuesta)
def crear_dispositivo(dispositivo: schemas.DispositivoCrear, db: Session = Depends(get_db)):
    return crud.create_dispositivo(db=db, dispositivo=dispositivo)

@app.get("/dispositivos/", response_model=List[schemas.DispositivoRespuesta])
def leer_dispositivos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_dispositivos(db, skip=skip, limit=limit)

@app.get("/dashboard")
def ver_dashboard(request: Request, db: Session = Depends(get_db)):
    equipos = crud.get_dispositivos(db)
    return templates.TemplateResponse("index.html", {"request": request, "dispositivos": equipos})

# --- FASE 6: NUEVA RUTA PARA GENERAR CONFIGURACIÓN MULTIVENDOR ---
@app.get("/dispositivos/{id}/config", response_class=PlainTextResponse)
def generar_configuracion(id: int, db: Session = Depends(get_db)):
    # Buscamos el equipo en la base de datos por su ID
    equipo = db.query(models.Dispositivo).filter(models.Dispositivo.id == id).first()
    
    if not equipo:
        raise HTTPException(status_code=404, detail="Dispositivo no encontrado")

    # LÓGICA DE RED: Generamos la plantilla según la marca
    if equipo.marca.lower() == "cisco":
        config = f"""! Plantilla generada para Cisco IOS/XE (Solo Lectura)
hostname {equipo.nombre}
!
interface GigabitEthernet0/0
 ip address {equipo.ip} 255.255.255.0
 no shutdown
!
! Configuracion Syslog
logging host 192.168.100.10
logging trap debugging
!
end"""
    elif equipo.marca.lower() == "fortinet":
        config = f"""# Plantilla generada para FortiOS (Solo Lectura)
config system global
    set hostname {equipo.nombre}
end
config log syslogd setting
    set status enable
    set server "192.168.100.10"
end"""
    elif equipo.marca.lower() == "huawei":
        config = f"""# Plantilla generada para Huawei VRP (Solo Lectura)
sysname {equipo.nombre}
#
info-center enable
info-center loghost 192.168.100.10
#
interface GigabitEthernet0/0/0
 ip address {equipo.ip} 255.255.255.0
#
return"""
    else:
        config = f"! No hay plantilla definida para la marca: {equipo.marca}"

    return config