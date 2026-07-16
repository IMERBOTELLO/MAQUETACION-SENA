from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database.dependencies import get_db
from backend.schemas.auth_shema import LoginRequest, LoginResponse
from backend.services.auth_service import autenticar_usuario

router = APIRouter(
    prefix = "/auth",
    tags = ["autenticacion"]
)

@router.post("/login", response_model = LoginResponse)
def login(datos: LoginRequest,db: Session = Depends(get_db)):
    
    usuario = autenticar_usuario(db, datos.correo, datos.contraseña, datos.rol)
    
    if usuario is None:
        raise HTTPException(
            status_code = 404, 
            detail = "El correo, la contraseña o el rol seleccionado son incorrectos."
        )
        
    return {
        "mensaje": "Usuario autenticado",
        "rol": usuario.rol  
    }