from pydantic import BaseModel
from datetime import date, time

# visualizacion de citas programadas
class  CitaProgramadasCreate(BaseModel):
    documento: str
    nombre_paciente: str
    especialista: str
    fecha: date
    hora: time
    servicio: str
    
class CitaProgramadasResponse(BaseModel):
    id_citas_programadas: int
    documento: str
    nombre_paciente: str
    especialista: str
    fecha: date
    hora: time
    servicio: str
    
    class Config:
        from_attributes = True
        