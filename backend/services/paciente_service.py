from sqlalchemy.orm import Session
from backend.models.paciente import Paciente
from backend.schemas.paciente_shema import PacienteCreate
from backend.models.usuario import Usuario
from backend.services.correo_service import enviar_correo

# importacion para crear contraseñas aleatorias
import secrets
import string

def generar_contraseña(longitud: int = 10):
    
    caracteres = (
        string.ascii_letters +
        string.digits +
        "!@#$%&*"
    )
    
    contraseña = "".join(
        secrets.choice(caracteres)
        for _ in range(longitud)
    )
    
    return contraseña

def crear_paciente(db: Session, paciente: PacienteCreate):

    nuevo_paciente = Paciente(
        nombres_paciente = paciente.nombres_paciente,
        apellidos_pacientes = paciente.apellidos_pacientes,
        fecha_nacimiento = paciente.fecha_nacimiento,
        numero_documento = paciente.numero_documento,
        correo = paciente.correo,
        fecha_registro = paciente.fecha_registro,
        telefono = paciente.telefono
    )

    # se agrega al usuario al que se le ha creado el paciente
    db.add(nuevo_paciente)
    
    # contraseña aleatoria
    contraseña_generada = generar_contraseña()
    
    # se crea automaticamente el usuario al que se le ha creado el paciente
    nuevo_usuario = Usuario(
        correo = paciente.correo,
        contraseña = contraseña_generada,
        rol = 'PACIENTE'
    )
    
    db.add(nuevo_usuario)
    
    # se envia correo a usuario
    enviar_correo(
        destinatario = paciente.correo,
        nombre = paciente.nombres_paciente,
        contraseña = contraseña_generada
    )
    
    # se guarda todo en una sola transicion del usuario creado
    db.commit()
    db.refresh(nuevo_paciente)

    return nuevo_paciente


def obtener_pacientes(db: Session):
    return db.query(Paciente).all()


def obtener_paciente_por_id(db: Session, id_paciente: int):
    return db.query(Paciente).filter(
        Paciente.id_paciente == id_paciente
    ).first()


# NUEVA FUNCION
def obtener_paciente_por_documento(db: Session, numero_documento: str):
    return db.query(Paciente).filter(
        Paciente.numero_documento == numero_documento
    ).first()


def actualizar_paciente(db: Session, id_paciente: int, paciente: PacienteCreate):

    paciente_db = db.query(Paciente).filter(
        Paciente.id_paciente == id_paciente
    ).first()

    if paciente_db is None:
        return None

    paciente_db.nombres_paciente = paciente.nombres_paciente
    paciente_db.apellidos_pacientes = paciente.apellidos_pacientes
    paciente_db.fecha_nacimiento = paciente.fecha_nacimiento
    paciente_db.numero_documento = paciente.numero_documento
    paciente_db.correo = paciente.correo
    paciente_db.fecha_registro = paciente.fecha_registro
    paciente_db.telefono = paciente.telefono

    db.commit()
    db.refresh(paciente_db)

    return paciente_db


def eliminar_paciente(db: Session, id_paciente: int):

    paciente_db = db.query(Paciente).filter(
        Paciente.id_paciente == id_paciente
    ).first()

    if paciente_db is None:
        return None

    db.delete(paciente_db)
    db.commit()

    return paciente_db