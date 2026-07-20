from sqlalchemy.orm import Session
from backend.models.resultado import Resultado
from backend.schemas.resultado_shema import ResultadoCreate

def crear_resultado(db: Session, resultado: ResultadoCreate):
    
    nuevo_resultado = Resultado(
        id_lab = resultado.id_lab,
        documento_paciente = resultado.documento_paciente,
        nombre_paciente = resultado.nombre_paciente,
        examen_medico = resultado.examen_medico,
        fecha_resultado = resultado.fecha_resultado,
        info_examen = resultado.info_examen,
        pdf = resultado.pdf,
        id_examen = resultado.id_examen
    )
    
    db.add(nuevo_resultado)
    db.commit()
    db.refresh(nuevo_resultado)
    return nuevo_resultado

def obtener_resultados(db: Session):
    return db.query(Resultado).all()

def obtener_resultado_por_id(db: Session, id_resultado: int):
    return db.query(Resultado).filter(
        Resultado.id_resultado == id_resultado
    ).first()
    
def actualizar_resultado(db: Session, id_resultado: int, resultado: ResultadoCreate):
    resultado_db = db.query(Resultado).filter(
        Resultado.id_resultado == id_resultado
    ).first()
    
    if resultado_db is None:
        return None
    
    resultado_db.id_lab = resultado.id_lab
    resultado_db.documento_paciente = resultado.documento_paciente
    resultado_db.nombre_paciente = resultado.nombre_paciente
    resultado_db.examen_medico = resultado.examen_medico
    resultado_db.fecha_resultado = resultado.fecha_resultado
    resultado_db.info_examen = resultado.info_examen
    resultado_db.pdf = resultado.pdf
    resultado_db.id_examen = resultado.id_examen
    
    db.commit()
    db.refresh(resultado_db)
    
    return resultado_db

def eliminar_resultado(db: Session, id_resultado: int):
    resultado_db = db.query(Resultado).filter(
        Resultado.id_resultado == id_resultado
    ).first()
    
    if resultado_db is None:
        return None
    
    db.delete(resultado_db)
    db.commit()
    
    return resultado_db