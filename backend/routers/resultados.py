from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database.dependencies import get_db
from backend.schemas.resultado_shema import ResultadoCreate, ResultadoResponse
from backend.services.resultado_service import crear_resultado, obtener_resultados, obtener_resultado_por_id, actualizar_resultado, eliminar_resultado
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