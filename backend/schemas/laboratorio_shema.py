from pydantic import BaseModel
from enum import Enum
from datetime import date

class tipo_examen(str, Enum):
    HEMOGRAMA_COMPLETO = 'HEMOGRAMA_COMPLETO'
    GLICEMIA = 'GLICEMIA'
    PERFIL_LIPIDICO = 'PERFIL_LIPIDICO'
    RADIOGRAFIA_DE_TORAX = 'RADIOGRAFIA_DE_TORAX'
    ECOGRAFIA_ABDOMINAL = 'ECOGRAFIA_ABDOMINAL'
    PRUEBA_DE_ESFUERZO = 'PRUEBA_DE_ESFUERZO'
    BIOMETRIA_HEMATICA = 'BIOMETRIA_HEMATICA'
    EXAMEN_DE_ORINA = 'EXAMEN_DE_ORINA'
    
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
