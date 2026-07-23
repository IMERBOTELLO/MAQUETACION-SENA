from sqlalchemy.orm import Session
from backend.models.laboratorio import Laboratorio
from backend.schemas.laboratorio_shema import LaboratorioCreate

def crear_laboratorio(db: Session, laboratorio: LaboratorioCreate):
    
    nuevo_laboratorio = Laboratorio(
        nombre_paciente = laboratorio.nombre_paciente,
        numero_documento = laboratorio.numero_documento,
        tipo_examen = laboratorio.tipo_examen,
        fecha = laboratorio.fecha,
        resultado = laboratorio.resultado
    )
    
    db.add(nuevo_laboratorio)
    db.commit()
    db.refresh(nuevo_laboratorio)
    return nuevo_laboratorio

def obtener_laboratorios(db: Session):
    return db.query(Laboratorio).all()

def obtener_laboratorio_por_id(db: Session, id_lab: int):
    return db.query(Laboratorio).filter(
        Laboratorio.id_lab == id_lab
    ).first()
    
def actualizar_laboratorio(db: Session, id_lab: int, laboratorio: LaboratorioCreate):
    laboratorio_db = db.query(Laboratorio).filter(
        Laboratorio.id_lab == id_lab
    ).first()
    
    if laboratorio_db is None:
        return None
    
    laboratorio_db.nombre_paciente = laboratorio.nombre_paciente
    laboratorio_db.numero_documento = laboratorio.numero_documento
    laboratorio_db.tipo_examen = laboratorio.tipo_examen
    laboratorio_db.fecha = laboratorio.fecha
    laboratorio_db.resultado = laboratorio.resultado
    
    db.commit()
    db.refresh(laboratorio_db)
    
    return laboratorio_db

def eliminar_laboratorio(db: Session, id_lab: int):
    laboratorio_db = db.query(Laboratorio).filter(
        Laboratorio.id_lab == id_lab
    ).first()
    
    if laboratorio_db is None:
        return None
    
    db.delete(laboratorio_db)
    db.commit()
    
    return laboratorio_db

