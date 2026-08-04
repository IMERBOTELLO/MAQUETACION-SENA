from sqlalchemy.orm import Session 
from backend.models.cita import Cita
from backend.models.paciente import Paciente
from backend.schemas.cita_shema import CitaCreate
from datetime import date

def crear_cita(db: Session, cita: CitaCreate):
    
    nueva_cita = Cita(
        nombre_paciente = cita.nombre_paciente,
        numero_documento_paciente = cita.numero_documento_paciente,
        id_medico = cita.id_medico,
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
    
def obtener_cita_por_documento(db: Session, numero_documento_paciente: str):
    return db.query(Cita).filter(
        Cita.numero_documento_paciente == numero_documento_paciente
    ).first()
    
def obtener_paciente_para_atencion(db: Session, numero_documento_paciente: str):
    
    cita = db.query(Cita).filter(
        Cita.numero_documento_paciente == numero_documento_paciente
    ).first()
    
    if cita is None:
        return None
    
    # buscar paciente
    
    paciente = db.query(Paciente).filter(
        Paciente.numero_documento == numero_documento_paciente
    ).first()
    
    if paciente is None:
        return None
    
    # calcular edad 
    
    hoy = date.today()
    
    edad = (
        hoy.year
        - paciente.fecha_nacimiento.year
        - (
            (hoy.month, hoy.day)
            <
            (paciente.fecha_nacimiento.month, 
             paciente.fecha_nacimiento.day)
        )
    )

    return {
        "nombre": paciente.nombres_paciente + " " + paciente.apellidos_pacientes,
        "edad": edad,
        "telefono": paciente.telefono
    }

def actualizar_cita(db: Session, id_cita: int, cita: CitaCreate):
    cita_db = db.query(Cita).filter(
        Cita.id_cita == id_cita
    ).first()
    
    if cita_db is None:
        return None
    
    cita_db.nombre_paciente = cita.nombre_paciente
    cita_db.numero_documento_paciente = cita.numero_documento_paciente
    cita_db.id_medico = cita_db.id_medico
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
    