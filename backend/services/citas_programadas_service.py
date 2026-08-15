from sqlalchemy.orm import Session
from backend.models.citas_programadas import CitaProgramadas
from backend.schemas.citas_programadas_shema import CitaProgramadasCreate

def create_cita(db: Session, citaprogramadas: CitaProgramadasCreate):
    db_cita = CitaProgramadas(
        documento = citaprogramadas.documento,
        nombre_paciente = citaprogramadas.nombre_paciente,
        especialista = citaprogramadas.especialista,
        fecha = citaprogramadas.fecha,
        hora = citaprogramadas.hora,
        servicio = citaprogramadas.servicio
    )
    db.add(db_cita)
    db.commit()
    db.refresh(db_cita)
    return db_cita

def mostrar_citas_programadas(db: Session):
    return db.query(CitaProgramadas).all()

def mostrar_citas_programadas_por_id(db: Session, id_citas_programadas: int):
    return db.query(CitaProgramadas).filter(
        CitaProgramadas.id_citas_programadas == id_citas_programadas
    ).first()
    
def actualizar_cita_programada(db: Session, id_citas_programadas: int, citaprogramadas: CitaProgramadasCreate):
    db_cita = db.query(CitaProgramadas).filter(
        CitaProgramadas.id_citas_programadas == id_citas_programadas
    ).first()
    
    if db_cita is None:
        return None
    
    db_cita.documento = citaprogramadas.documento
    db_cita.nombre_paciente = citaprogramadas.nombre_paciente
    db_cita.especialista = citaprogramadas.especialista
    db_cita.fecha = citaprogramadas.fecha
    db_cita.hora = citaprogramadas.hora
    db_cita.servicio = citaprogramadas.servicio
    
    db.commit()
    db.refresh(db_cita)
    
    return db_cita

def eleminar_cita_programada(db: Session, id_citas_programadas: int):
    db_cita = db.query(CitaProgramadas).filter(
        CitaProgramadas.id_citas_programadas == id_citas_programadas
    ).first()
    
    if db_cita is None:
        return None
    
    db.delete(db_cita)
    db.commit()
    
    return db_cita