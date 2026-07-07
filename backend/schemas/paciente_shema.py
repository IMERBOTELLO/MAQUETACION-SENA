from pydantic import BaseModel
from datetime import date

class PacienteCreate(BaseModel):
    nombres_paciente: str
    apellidos_pacientes: str
    fecha_nacimiento: date
    numero_documento: str
    correo: str
    fecha_registro: date
    telefono: str
    
class PacienteResponse(PacienteCreate):
    id_paciente: int
    
    class Config:
        from_attributes = True