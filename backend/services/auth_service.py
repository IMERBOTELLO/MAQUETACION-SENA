from sqlalchemy.orm import Session
from backend.models.usuario import Usuario

def autenticar_usuario(db: Session, usuario: str, contraseña: str, rol: str):
    
    usuario = (
        db.query(Usuario)
        .filter(
            Usuario.correo == usuario,
            Usuario.contraseña == contraseña,
            Usuario.rol == rol
        )
        .first()
    )
    return usuario