from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database.dependencies import get_db
from backend.schemas.cita_shema import CitaCreate, CItaResponse
from backend.services.cita_service import crear_cita, obtener_cita, obtener_cita_por_id, actualizar_cita, eliminar_cita
from typing import List

router = APIRouter(
    prefix="/citas",
    tags=["citas"]
)

@router.post("/", response_model = CItaResponse)
def crear(
    cita: CitaCreate,
    db: Session = Depends(get_db)
):
    return crear_cita(db, cita)

@router.get("/", response_model = List[CItaResponse])
def listar_citas(db: Session = Depends(get_db)):
    return obtener_cita(db)

@router.get("/{id_cita}", response_model = CItaResponse)
def buscar_cita(id_cita: int, db: Session = Depends(get_db)):
    cita = obtener_cita_por_id(db, id_cita)
    
    if cita is None:
        raise HTTPException(
            status_code = 404, 
            detail = "No existe la cita con ese id"
        )
    
    return cita

@router.put("/{id_cita}", response_model = CItaResponse)
def actualizar(
    id_cita: int, 
    cita: CitaCreate, 
    db: Session = Depends(get_db)
):
    actualizar = actualizar_cita(db, id_cita, cita)
    
    if actualizar is None:
        raise HTTPException(
            status_code = 404,
            detail = "No existe la cita con ese id"
        )
        
    return actualizar
        
@router.delete("/{id_cita}", response_model = CItaResponse)
def eliminar(
    id_cita: int,
    db: Session = Depends(get_db)
):
    eliminar = eliminar_cita(db, id_cita)
    
    if eliminar is None:
        raise HTTPException(
            status_code = 404,
            detail = "No existe la cita con ese id"
        )
    
    return eliminar