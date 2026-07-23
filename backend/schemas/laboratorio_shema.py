from pydantic import BaseModel
from enum import Enum
from datetime import date

class tipo_examen(str, Enum):
    SANGRE = 'SANGRE'
    HORINA = 'HORINA'
    COVID = 'COVID'
    RADIOGRAFIA = 'RADIOGRAFIA'
    
class LaboratorioCreate(BaseModel):
    nombre_paciente: str
    numero_documento: str
    tipo_examen: tipo_examen
    fecha: date
    resultado: str
    
class LaboratorioResponse(BaseModel):
    id_lab: int
    nombre_paciente: str
    numero_documento: str
    tipo_examen: tipo_examen
    fecha: date
    resultado: str
    
    class Config:
        from_attributes = True
