from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class DispositivoBase(BaseModel):
    nombre: str = Field(..., max_length=50)
    ip: str = Field(..., max_length=15)
    marca: str = Field(..., max_length=20)
    modelo: str = Field(..., max_length=50)

class DispositivoCrear(DispositivoBase):
    pass

class DispositivoRespuesta(DispositivoBase):
    id: int
    estado: str
    fecha_actualizacion: datetime

    class Config:
        from_attributes = True

class EventoBase(BaseModel):
    origen_ip: str = Field(..., max_length=15)
    severidad: int = Field(..., ge=0, le=7)
    mensaje: str = Field(..., max_length=500)

class EventoCrear(EventoBase):
    dispositivo_id: int

class EventoRespuesta(EventoBase):
    id: int
    dispositivo_id: int
    timestamp: str
    es_sintetico: bool

    class Config:
        from_attributes = True
        