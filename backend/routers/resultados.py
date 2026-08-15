from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database.dependencies import get_db
from backend.schemas.resultado_shema import ResultadoCreate, ResultadoResponse, EntregaResultadoResponse
from backend.services.resultado_service import crear_resultado, obtener_resultados, obtener_resultado_por_id, actualizar_resultado, eliminar_resultado, obtener_datos_entrega, obtener_pdf_resultado, enviar_resultado_por_correo 
from typing import List

router = APIRouter(
    prefix = "/resultados",
    tags = ["resultados"]
)

@router.post("/", response_model = ResultadoResponse)
def crear(
    resultado: ResultadoCreate,
    db: Session = Depends(get_db)
):
    return crear_resultado(db, resultado)

@router.get("/", response_model = List[ResultadoResponse])
def listar_resultados(db: Session = Depends(get_db)):
    return obtener_resultados(db)

@router.get("/registrados", response_model = List[ResultadoResponse])
def listar_resultados_registrados(db: Session = Depends(get_db)):
    return obtener_resultados(db)

@router.get("/{id_resultado}", response_model = ResultadoResponse)
def buscar_resultado(
    id_resultado: int, 
    db: Session = Depends(get_db)
):
    resultado = obtener_resultado_por_id(db, id_resultado)
    
    if resultado is None:
        raise HTTPException(
            status_code = 404,
            detail = "Resultado no encontrado"
        )
        
    return resultado

# crear enpoint para buscar el paciente, verificar que tenga un resultado registrado, obtener el pdf, obtener el correo y el nombre del paciente

@router.get("/entrega/{documento}", response_model = EntregaResultadoResponse)
def obtener_entregar(
    documento: str,
    db: Session = Depends(get_db)
):
    
    return obtener_datos_entrega(documento, db)

@router.get("/pdf/{id_resultado}")
def obtener_pdf(
    id_resultado: int,
    db: Session = Depends(get_db)
):
    return obtener_pdf_resultado(id_resultado, db)

@router.post("/enviar-correo/{id_resultado}")
def enviar_correo_resultado(
    id_resultado: int,
    db: Session = Depends(get_db)
):
    return enviar_resultado_por_correo(db, id_resultado)

@router.put("/{id_resultado}", response_model = ResultadoResponse)
def actualizar(
    id_resultado: int,
    resultado: ResultadoCreate,
    db: Session = Depends(get_db)
):
    resultado_actualizado = actualizar_resultado(db, id_resultado, resultado)
    
    if resultado_actualizado is None:
        raise HTTPException(
            status_code = 404,
            detail = "Resultado no encontrado"
        )
        
    return resultado_actualizado

@router.delete("/{id_resultado}", response_model = ResultadoResponse)
def eliminar(
    id_resultado: int,
    db: Session = Depends(get_db)
):
    resultado_eliminado = eliminar_resultado(db, id_resultado)
    
    if resultado_eliminado is None:
        raise HTTPException(
            status_code = 404,
            detail = "Resultado no encontrado"
        )
        
    return resultado_eliminado