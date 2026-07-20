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
    usuario_db = db.query(Resultado).filter(
        Resultado.id_resultado == id_resultado
    ).first()
    
    if usuario_db is None:
        return None
    
    usuario_db.id_lab = resultado.id_lab
    usuario_db.documento_paciente = resultado.documento_paciente
    usuario_db.nombre_paciente = resultado.nombre_paciente
    usuario_db.examen_medico = resultado.examen_medico
    usuario_db.fecha_resultado = resultado.fecha_resultado
    usuario_db.info_examen = resultado.info_examen
    usuario_db.pdf = resultado.pdf
    usuario_db.id_examen = resultado.id_examen
    
    db.commit()
    db.refresh(usuario_db)
    
    return usuario_db

def eliminar_resultado(db: Session, id_resultado: int):
    resultado_db = db.query(Resultado).filter(
        Resultado.id_resultado == id_resultado
    ).first()
    
    if resultado_db is None:
        return None
    
    db.delete(resultado_db)
    db.commit()
    
    return resultado_db