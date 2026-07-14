from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from backend.database.dependencies import get_db
from backend.schemas.paciente_shema import PacienteCreate, PacienteResponse
from backend.services.paciente_service import (
    crear_paciente,
    obtener_pacientes,
    obtener_paciente_por_id,
    obtener_paciente_por_documento,
    actualizar_paciente,
    eliminar_paciente
)

router = APIRouter(
    prefix="/pacientes",
    tags=["pacientes"]
)


@router.post("/", response_model=PacienteResponse)
def crear(
    paciente: PacienteCreate,
    db: Session = Depends(get_db)
):
    return crear_paciente(db, paciente)


@router.get("/", response_model=List[PacienteResponse])
def listar_pacientes(db: Session = Depends(get_db)):
    return obtener_pacientes(db)


# NUEVO ENDPOINT PARA BUSCAR POR NUMERO DE DOCUMENTO
@router.get("/documento/{numero_documento}", response_model=PacienteResponse)
def buscar_por_documento(
    numero_documento: str,
    db: Session = Depends(get_db)
):
    paciente = obtener_paciente_por_documento(db, numero_documento)

    if paciente is None:
        raise HTTPException(
            status_code=404,
            detail="Paciente no encontrado"
        )

    return paciente


@router.get("/{id_paciente}", response_model=PacienteResponse)
def buscar_paciente(
    id_paciente: int,
    db: Session = Depends(get_db)
):
    paciente = obtener_paciente_por_id(db, id_paciente)

    if paciente is None:
        raise HTTPException(
            status_code=404,
            detail="Paciente no encontrado"
        )

    return paciente


@router.put("/{id_paciente}", response_model=PacienteResponse)
def actualizar(
    id_paciente: int,
    paciente: PacienteCreate,
    db: Session = Depends(get_db)
):
    paciente_actualizado = actualizar_paciente(db, id_paciente, paciente)

    if paciente_actualizado is None:
        raise HTTPException(
            status_code=404,
            detail="Paciente no encontrado con el id"
        )

    return paciente_actualizado


@router.delete("/{id_paciente}", response_model=PacienteResponse)
def eliminar(
    id_paciente: int,
    db: Session = Depends(get_db)
):
    paciente_eliminado = eliminar_paciente(db, id_paciente)

    if paciente_eliminado is None:
        raise HTTPException(
            status_code=404,
            detail="Paciente no encontrado por el id"
        )

    return paciente_eliminado