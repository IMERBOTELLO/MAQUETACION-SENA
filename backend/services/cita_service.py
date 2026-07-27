from sqlalchemy.orm import Session 
from backend.models.cita import Cita
from backend.schemas.cita_shema import CitaCreate

def crear_cita(db: Session, cita: CitaCreate):
    
    nueva_cita = Cita(
        nombre_paciente = cita.nombre_paciente,
        numero_documento_paciente = cita.numero_documento_paciente,
        especialista = cita.especialista,
        fecha = cita.fecha,
        hora = cita.hora,
        servicio = cita.servicio
    )
    
    db.add(nueva_cita)
    db.commit()
    db.refresh(nueva_cita)    
    return nueva_cita

def obtener_cita(db: Session):
    return db.query(Cita).all()

def obtener_cita_por_id(db: Session, id_cita: int):
    return db.query(Cita).filter(
        Cita.id_cita == id_cita
    ).first()
    
def actualizar_cita(db: Session, id_cita: int, cita: CitaCreate):
    cita_db = db.query(Cita).filter(
        Cita.id_cita == id_cita
    ).first()
    
    if cita_db is None:
        return None
    
    cita_db.nombre_paciente = cita.nombre_paciente
    cita_db.numero_documento_paciente = cita.numero_documento_paciente
    cita_db.especialista = cita.especialista
    cita_db.fecha = cita.fecha
    cita_db.hora = cita.hora
    cita_db.servicio = cita.servicio
    
    db.commit()
    db.refresh(cita_db)
    
    return cita_db

def eliminar_cita(db: Session, id_cita: int):
    cita_db = db.query(Cita).filter(
        Cita.id_cita == id_cita
    ).first()
    
    if cita_db is None:
        return None
    
    db.delete(cita_db)
    db.commit()
    
    return cita_db
    