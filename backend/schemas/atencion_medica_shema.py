from pydantic import BaseModel
from datetime import date


class AtencionMedicaBase(BaseModel):
    diagnostico: str
    observaciones: str
    fecha_atencion: date
    numero_documento: str
    examenes: str


class AtencionMedicaCreate(AtencionMedicaBase):
    pass


class AtencionMedicaResponse(AtencionMedicaBase):
    id_atencion: int

    class Config:
        from_attributes = True