from pydantic import BaseModel, EmailStr
from backend.schemas.usuario_shema import RolUsuario

class LoginRequest(BaseModel):
    correo: EmailStr
    contraseña: str
    rol: RolUsuario
    
class LoginResponse(BaseModel):
    mensaje: str
    rol: str
