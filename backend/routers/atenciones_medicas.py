from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database.dependencies import get_db
from backend.schemas.atencion_medica_shema import (
    AtencionMedicaCreate,
    AtencionMedicaResponse,
)
from backend.services.atencion_service import (
    crear_atencion,
    obtener_atenciones,
    obtener_atencion_por_id,
)

router = APIRouter(
    prefix="/atenciones_medicas",
    tags=["Atenciones Médicas"]
)


@router.post("/", response_model=AtencionMedicaResponse)
def crear(atencion: AtencionMedicaCreate, db: Session = Depends(get_db)):
    return crear_atencion(db, atencion)


@router.get("/", response_model=list[AtencionMedicaResponse])
def listar(db: Session = Depends(get_db)):
    return obtener_atenciones(db)


@router.get("/{id_atencion}", response_model=AtencionMedicaResponse)
def obtener(id_atencion: int, db: Session = Depends(get_db)):
    return obtener_atencion_por_id(db, id_atencion)