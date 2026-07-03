from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database.dependencies import get_db
from backend.schemas.usuario_shema import UsuarioCreate, UsuarioResponse
from backend.services.usuario_service import crear_usuario, obtener_usuarios, obtener_usuario_por_id, actualizar_usuario, eliminar_usuario
from typing import List

router = APIRouter(
    prefix = "/usuarios",
    tags = ["usuarios"]
)

@router.post("/", response_model = UsuarioResponse)
def crear(
    usuario: UsuarioCreate,
    db: Session = Depends(get_db)
):
    return crear_usuario(db, usuario)

@router.get("/", response_model = List[UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    return obtener_usuarios(db)

@router.get("/{id_usuario}", response_model = UsuarioResponse)
def buscar_usuario(id_usuario: int, db: Session = Depends(get_db)):
    usuario = obtener_usuario_por_id(db, id_usuario)
    
    if usuario is None:
        raise HTTPException(
            status_code = 404, 
            detail = "Usuario no encontrado"
        )
    
    return usuario

@router.put("/{id_usuario}", response_model = UsuarioResponse)
def actualizar(
    id_usuario: int,
    usuario: UsuarioCreate,
    db: Session = Depends(get_db)
):
    usuario_actualizado = actualizar_usuario(db, id_usuario, usuario)
    
    if usuario_actualizado is None:
        raise HTTPException(
            status_code = 404,
            detail = "Usuario no encontrado"
        )
    
    return usuario_actualizado

@router.delete("/{id_usuario}", response_model = UsuarioResponse)
def eliminar(
    id_usuario: int,
    db: Session = Depends(get_db)
):
    
    usuario_eliminado = eliminar_usuario(db, id_usuario)
    
    if usuario_eliminado is None:
        raise HTTPException(
            status_code = 404,
            detail = "Usuario no encontrado"
        )
        
    return usuario_eliminado