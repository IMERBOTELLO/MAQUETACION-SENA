from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from backend.database.dependencies import get_db
from backend.schemas.medico_shema import (
    MedicoCreate,
    MedicoResponse
)
from backend.services.medico_service import (
    crear_medico,
    obtener_medicos,
    obtener_medico_por_id,
    actualizar_medico,
    eliminar_medico
)

router = APIRouter(
    prefix="/medicos",
    tags=["Medicos"]
)

@router.post("/", response_model=MedicoResponse)
def crear(
    medico: MedicoCreate,
    db: Session = Depends(get_db)
):
    return crear_medico(db, medico)


@router.get("/", response_model=List[MedicoResponse])
def listar(
    db: Session = Depends(get_db)
):
    return obtener_medicos(db)


@router.get("/{id_medico}", response_model=MedicoResponse)
def buscar(
    id_medico: int,
    db: Session = Depends(get_db)
):
    medico = obtener_medico_por_id(db, id_medico)

    if medico is None:
        raise HTTPException(
            status_code=404,
            detail="Médico no encontrado"
        )

    return medico


@router.put("/{id_medico}", response_model=MedicoResponse)
def actualizar(
    id_medico: int,
    medico: MedicoCreate,
    db: Session = Depends(get_db)
):
    medico_actualizado = actualizar_medico(db, id_medico, medico)

    if medico_actualizado is None:
        raise HTTPException(
            status_code=404,
            detail="Médico no encontrado"
        )

    return medico_actualizado


@router.delete("/{id_medico}", response_model=MedicoResponse)
def eliminar(
    id_medico: int,
    db: Session = Depends(get_db)
):
    medico = eliminar_medico(db, id_medico)

    if medico is None:
        raise HTTPException(
            status_code=404,
            detail="Médico no encontrado"
        )

    return medico 