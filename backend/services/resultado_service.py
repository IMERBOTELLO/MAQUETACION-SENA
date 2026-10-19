from sqlalchemy.orm import Session
from backend.models.resultado import Resultado
from backend.schemas.resultado_shema import ResultadoCreate
from backend.models.paciente import Paciente
from fastapi import HTTPException
from fastapi.responses import Response
import base64
from backend.services.correo_service import enviar_resultado_correo

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
    
def obtener_datos_entrega(documento: str, db):
    
    resultado = (
        db.query(Resultado, Paciente)
        .join(
            Paciente,
            Resultado.documento_paciente == Paciente.numero_documento
        )
        .filter(
            Resultado.documento_paciente == documento
        )
        .first()
    )
    
    if resultado is None:
        raise HTTPException(
            status_code = 404,
            detail = "El paciente no tiene resultados registrados"
        )
        
    resultado_db, paciente = resultado
    
    return {
        "documento": paciente.numero_documento,
        "nombre_paciente": paciente.nombres_paciente,
        "correo": paciente.correo,
        "id_resultado": resultado_db.id_resultado
    }
    
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

def obtener_pdf_resultado(id_resultado: int, db):
    
    resultado = (
        db.query(Resultado)
        .filter(Resultado.id_resultado == id_resultado)
        .first()
    )
    
    if resultado is None:
        
        raise HTTPException(
            status_code = 404,
            detail = "Resultado no encontrado"
        )
        
    pdf_bytes = base64.b64decode(resultado.pdf)
        
    return Response(
        content = pdf_bytes,
        media_type = "application/pdf",
        headers = {
            "Content-Disposition":
            f'inline; filename="resultado_{id_resultado}.pdf"'
        }
    )
    
def enviar_resultado_por_correo(db: Session, id_resultado: int):
    
    resultado = (
        db.query(Resultado)
        .filter(Resultado.id_resultado == id_resultado)
        .first()
    )
    
    if resultado is None:
        raise HTTPException(
            status_code = 404,
            detail = "Resultado no encontrado"
        )
        
    paciente = (
        db.query(Paciente)
        .filter(
            Paciente.numero_documento == resultado.documento_paciente
        )
        .first()
    )
    
    if paciente is None:
        raise HTTPException(
            status_code = 404,
            detail = "Paciente no encontrado"
        )
        
    if not paciente.correo:
        raise HTTPException(
            status_code = 404,
            detail = "Correo no encontrado"
        )
    
    if not resultado.pdf:
        raise HTTPException(
            status_code = 404,
            detail = "PDF no encontrado"
        )
        
    envio_exitoso = enviar_resultado_correo(
    destinatario=paciente.correo,
    nombre=paciente.nombres_paciente,
    documento=paciente.numero_documento,
    pdf_base64=resultado.pdf
)

    if not envio_exitoso:
        raise HTTPException(
            status_code=502,
            detail="No fue posible enviar el correo con el resultado médico"
        )

    return {
        "mensaje": "Correo enviado con resultado exitosamente",
        "correo": paciente.correo,
        "documento": paciente.numero_documento
    }