from pydantic import BaseModel
from datetime import date

class PacienteCreate(BaseModel):
    nombres_paciente: str
    apellidos_pacientes: str
    fecha_nacimiento: date
    numero_documento: int
    correo: str
    fecha_registro: date
    telefono: int

class PacienteResponse(PacienteCreate):
    id_paciente: int

    class Config:
        from_attributes = True