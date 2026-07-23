from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database.dependencies import get_db
from backend.schemas.laboratorio_shema import LaboratorioCreate, LaboratorioResponse
from backend.services.laboratorio_service import crear_laboratorio, obtener_laboratorios, obtener_laboratorio_por_id, actualizar_laboratorio, eliminar_laboratorio, obtener_laboratorio_por_numero_documento
from typing import List

router = APIRouter(
    prefix = "/laboratorios",
    tags = ["laboratorios"]
)

@router.post("/", response_model = LaboratorioResponse)
def crear(
    laboratorio: LaboratorioCreate,
    db: Session = Depends(get_db)
):
    return crear_laboratorio(db, laboratorio)

@router.get("/", response_model = List[LaboratorioResponse])
def listar_laboratorios(db: Session = Depends(get_db)):
    return obtener_laboratorios(db)

@router.get("/documento/{documento}", response_model=LaboratorioResponse)
def buscar_por_documento(
    documento: int,
    db: Session = Depends(get_db)
):
    laboratorio = obtener_laboratorio_por_numero_documento(db, documento)

    if laboratorio is None:
        raise HTTPException(
            status_code=404,
            detail="Laboratorio no encontrado"
        )

    return laboratorio

@router.get("/{id_lab}", response_model = LaboratorioResponse)
def buscar_laboratorio(id_lab: int, db: Session = Depends(get_db)):
    laboratorio = obtener_laboratorio_por_id(db, id_lab)
    
    if laboratorio is None:
        raise HTTPException(
            status_code = 404,
            detail = "Laboratorio no encontrado"
        )
        
    return laboratorio

@router.put("/{id_lab}", response_model = LaboratorioResponse)
def actualizar(
    id_lab: int,
    laboratorio: LaboratorioCreate,
    db: Session = Depends(get_db)
):
    laboratorio_actualizado = actualizar_laboratorio(db, id_lab, laboratorio)
    
    if laboratorio_actualizado is None:
        raise HTTPException(
            status_code = 404,
            detail = "Laboratorio no encontrado"
        )
        
    return laboratorio_actualizado

@router.delete("/{id_lab}", response_model = LaboratorioResponse)
def eliminar(
    id_lab: int,
    db: Session = Depends(get_db)
):
    laboratorio_eliminado = eliminar_laboratorio(db, id_lab)
    
    if laboratorio_eliminado is None:
        raise HTTPException(
            status_code = 404,
            detail = "Laboratorio no encontrado"
        )
        
    return laboratorio_eliminado