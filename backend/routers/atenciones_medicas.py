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
    obtener_atencion_por_numero_documento
)

from backend.services.atencion_service import obtener_documento_para_laboratorio

from fastapi import HTTPException

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

@router.get("/documento/{documento}", response_model=AtencionMedicaResponse)
def buscar_por_documento(
    documento: int,
    db: Session = Depends(get_db)
):
    atencion = obtener_atencion_por_numero_documento(db, documento)

    if atencion is None:
        raise HTTPException(
            status_code=404,
            detail="Atención médica no encontrada"
        )

    return atencion

@router.get("/{id_atencion}", response_model=AtencionMedicaResponse)
def obtener(id_atencion: int, db: Session = Depends(get_db)):
    return obtener_atencion_por_id(db, id_atencion)

@router.get("/laboratorio/{numero_documento}/")
def obtener_datos(
    numero_documento: str,
    db: Session = Depends(get_db)
):
    
    datos = obtener_documento_para_laboratorio(db, numero_documento)
    
    if datos is None:
        raise HTTPException(
            status_code=404,
            detail="Atención médica no encontrada para este documento"
        )
        
    return datos