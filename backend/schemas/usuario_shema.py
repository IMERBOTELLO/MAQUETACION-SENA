from pydantic import BaseModel
from enum import Enum

# crear usuario
class RolUsuario(str, Enum):
    RECEPCIONISTA = 'RECEPCIONISTA'
    MEDICO = 'MEDICO'
    LABORATORIO = 'LABORATORIO'
    PACIENTE = 'PACIENTE'
    ADMINISTRADOR = 'ADMINISTRADOR'
    
class UsuarioCreate(BaseModel):
    correo: str
    contraseña: str
    rol: RolUsuario
    
class UsuarioLogin(BaseModel):
    rol: RolUsuario
    correo: str
    contraseña: str
    
class UsuarioResponse(BaseModel):
    id_usuario: int
    correo: str
    rol: RolUsuario

    class Config:
        from_attributes = True
    