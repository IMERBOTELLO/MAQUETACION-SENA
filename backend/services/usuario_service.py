from sqlalchemy.orm import Session
from backend.models.usuario import Usuario
from backend.schemas.usuario_shema import UsuarioCreate

def crear_usuario(db: Session, usuario: UsuarioCreate):
    
    nuevo_usuario = Usuario(
        rol = usuario.rol,
        correo = usuario.correo,
        contraseña = usuario.contraseña
    )
    
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario