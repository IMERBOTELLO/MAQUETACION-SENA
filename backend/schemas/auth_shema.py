from pydantic import BaseModel, EmailStr

class LoginRequest(BaseModel):
    correo: EmailStr
    contraseña: str
    
class LoginResponse(BaseModel):
    mensaje: str
    rol: str
