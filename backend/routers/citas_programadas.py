from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database.dependencies import get_db
from backend.schemas.citas_programadas_shema import CitaProgramadasCreate, CitaProgramadasResponse
from backend.services.citas_programadas_service import create_cita, mostrar_citas_programadas, mostrar_citas_programadas_por_id, actualizar_cita_programada, eleminar_cita_programada
from typing import List

router = APIRouter(
    prefix="/citas_programadas",
    tags=["Citas Programadas"],
)

@router.post("/", response_model=CitaProgramadasResponse)
def create_cita_programada(
    citaprogramadas: CitaProgramadasCreate,
    db: Session = Depends(get_db),
):
    return create_cita(db, citaprogramadas)

@router.get("/", response_model = List[CitaProgramadasResponse])
def listar_citas_programadas(db: Session = Depends(get_db)):
    return mostrar_citas_programadas(db)

@router.get("/{id_citas_programadas}", response_model = CitaProgramadasResponse)
def buscar_citas_programadas_por_id(id_citas_programadas: int, db: Session = Depends(get_db)):
    mostrar = mostrar_citas_programadas_por_id(db, id_citas_programadas)
    
    if mostrar is None:
        raise HTTPException(
            status_code = 404,
            detail = "No exise cita programada con ese id"
        )
        
    return mostrar

@router.put("/{id_citas_programadas}", response_model = CitaProgramadasResponse)
def actualizar(
    id_citas_programadas: int,
    citaprogramadas: CitaProgramadasCreate,
    db: Session = Depends(get_db),
):
    actuaizar = actualizar_cita_programada(db, id_citas_programadas, citaprogramadas)
    
    if actuaizar is None:
        raise HTTPException(
            status_code = 404,
            detail = "No exise cita programada con ese id"
        )
        
    return actuaizar

@router.delete("/{id_citas_programadas}", response_model = CitaProgramadasResponse)
def eliminar(
    id_citas_programadas: int,
    db: Session = Depends(get_db),
):
    eliminar = eleminar_cita_programada(db, id_citas_programadas)
    
    if eliminar is None:
        raise HTTPException(
            status_code = 404,
            detail = "No exise cita programada con ese id"
        )
        
    return eliminar