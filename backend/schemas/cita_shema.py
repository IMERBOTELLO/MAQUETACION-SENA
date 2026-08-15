from pydantic import BaseModel
from datetime import date, time
from enum import Enum

# crear servicio
class Servicio(str, Enum):
    CARDIOLOGIA = 'CARDIOLOGIA'
    PEDIATRIA = 'PEDIATRIA'
    GINECOLOGIA = 'GINECOLOGIA'
    MEDICINA_INTERNA = 'MEDICINA_INTERNA'
    CIRUGIA_GENERAL = 'CIRUGIA_GENERAL'
    ORTOPEDIA = 'ORTOPEDIA'
    TRAUMATOLOGIA = 'TRAUMATOLOGIA'
    DERMATOLOGIA = 'DERMATOLOGIA'

# crear cita
class CitaCreate(BaseModel):
    nombre_paciente: str
    numero_documento_paciente: int
    fecha: date
    hora: time
    servicio: Servicio
    id_medico: int
    
class CItaResponse(BaseModel):
    id_cita: int
    nombre_paciente: str
    numero_documento_paciente: int
    fecha: date
    hora: time
    servicio: Servicio
    id_medico: int
    
    class Config:
        from_attributes = True