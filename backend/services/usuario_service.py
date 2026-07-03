from sqlalchemy.orm import Session
from backend.models.usuario import Usuario
from backend.schemas.usuario_shema import UsuarioCreate
from typing import Optional

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

def obtener_usuarios(db: Session):
    return db.query(Usuario).all()

def obtener_usuario_por_id(db: Session, id_usuario: int):
    return db.query(Usuario).filter(
        Usuario.id_usuario == id_usuario
    ).first()

def actualizar_usuario(db: Session, id_usuario: int, usuario: UsuarioCreate):
    usuario_db = db.query(Usuario).filter(
        Usuario.id_usuario == id_usuario    
    ).first()
    
    if usuario_db is None:
        return None
    
    usuario_db.rol = usuario.rol
    usuario_db.correo = usuario.correo
    usuario_db.contraseña = usuario.contraseña
    
    db.commit()
    db.refresh(usuario_db)
    
    return usuario_db

def eliminar_usuario(db: Session, id_usuario: int):
    usuario_db = db.query(Usuario).filter(
        Usuario.id_usuario == id_usuario
    ).first()
    
    if usuario_db is None:
        return None
    
    db.delete(usuario_db)
    db.commit()
    
    return usuario_db
    
    