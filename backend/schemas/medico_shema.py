from pydantic import BaseModel

class MedicoBase(BaseModel):
    nombre_medico: str
    especialidad: str
    telefono: str
    correo: str

class MedicoCreate(MedicoBase):
    pass

class MedicoUpdate(MedicoBase):
    pass

class MedicoResponse(BaseModel):
    id_medico: int
    nombre_medico: str
    especialidad: str
    telefono: str
    correo: str

    class Config:
        from_attributes = True