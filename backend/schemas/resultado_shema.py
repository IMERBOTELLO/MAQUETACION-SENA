from pydantic import BaseModel
from enum import Enum
from datetime import date

# crear resultado
class examen_medico(str, Enum):
    HEMOGRAMA_COMPLETO = 'HEMOGRAMA_COMPLETO'
    GLICEMIA = 'GLICEMIA'
    PERFIL_LIPIDICO = 'PERFIL_LIPIDICO'
    RADIOGRAFIA_DE_TORAX = 'RADIOGRAFIA_DE_TORAX'
    ECOGRAFIA_ABDOMINAL = 'ECOGRAFIA_ABDOMINAL'
    PRUEBA_DE_ESFUERZO = 'PRUEBA_DE_ESFUERZO'
    BIOMETRIA_HEMATICA = 'BIOMETRIA_HEMATICA'
    EXAMEN_DE_ORINA = 'EXAMEN_DE_ORINA'
    
class ResultadoCreate(BaseModel):
    id_lab: int
    documento_paciente: int
    nombre_paciente: str
    examen_medico: examen_medico
    fecha_resultado: date
    info_examen: str
    pdf: bytes
    id_examen: int
    
class ResultadoResponse(BaseModel):
    id_resultado: int
    id_lab: int
    documento_paciente: int
    nombre_paciente: str
    examen_medico: examen_medico
    fecha_resultado: date
    info_examen: str
    pdf: bytes
    id_examen: int
    
    class Config:
        from_attributes = True