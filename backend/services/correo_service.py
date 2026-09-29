import os
import resend
import logging

logger = logging.getLogger(__name__)

# Configuración desde variables de entorno
RESEND_API_KEY = os.getenv("re_BJAKUpor_8DdTk6MRyTxM1LMn8TAyat5j")
FROM_EMAIL = os.getenv("FROM_EMAIL", "hospisfot@gmail.com")

if RESEND_API_KEY:
    resend.api_key = RESEND_API_KEY


def enviar_correo(destinatario: str, nombre: str, contraseña: str) -> bool:
    """
    Envía correo de bienvenida vía Resend API.
    Returns True si se envió, False si falló (NO lanza excepción).
    """
    if not RESEND_API_KEY:
        logger.warning("RESEND_API_KEY no configurado, omitiendo envío")
        return False

    try:
        params = {
            "from": f"HOSPISOFT <{FROM_EMAIL}>",
            "to": [destinatario],
            "subject": "Bienvenido a HOSPISOFT",
            "html": f"""
                <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
                    <h2 style="color: #2563eb;">¡Bienvenido a HOSPISOFT!</h2>
                    <p>Hola <strong>{nombre}</strong>,</p>
                    <p>Su cuenta ha sido creada correctamente.</p>
                    <div style="background: #f3f4f6; padding: 20px; border-radius: 8px; margin: 20px 0;">
                        <p><strong>Credenciales de acceso:</strong></p>
                        <p>Correo: <code>{destinatario}</code></p>
                        <p>Contraseña: <code>{contraseña}</code></p>
                    </div>
                    <p style="color: #6b7280; font-size: 14px;">
                        Le damos la bienvenida a nuestro sistema de atención.
                    </p>
                    <hr style="border: none; border-top: 1px solid #e5e7eb; margin: 20px 0;">
                    <p style="color: #9ca3af; font-size: 12px;">Equipo HOSPISOFT</p>
                </div>
            """,
            "text": f"""
Hola {nombre},

Su cuenta ha sido creada correctamente.

Credenciales de acceso:
Correo: {destinatario}
Contraseña: {contraseña}

Le damos la bienvenida a nuestro sistema de atención.

Saludos,
Equipo HOSPISOFT
            """
        }

        response = resend.Emails.send(params)
        
        if response.get("id"):
            logger.info(f"✅ Correo enviado a {destinatario} (id: {response['id']})")
            return True
        else:
            logger.error(f"❌ Resend respondió sin ID: {response}")
            return False

    except Exception as e:
        logger.error(f"⚠️ Error Resend enviando a {destinatario}: {e}")
        return False


def enviar_resultado_correo(destinatario: str, nombre: str, documento: str, pdf_base64: str) -> bool:
    """
    Envía resultado médico con PDF adjunto vía Resend.
    """
    if not RESEND_API_KEY:
        logger.warning("RESEND_API_KEY no configurado, omitiendo envío de resultado")
        return False

    try:
        import base64
        
        # Decodificar PDF
        if isinstance(pdf_base64, str):
            pdf_bytes = base64.b64decode(pdf_base64)
        else:
            pdf_bytes = pdf_base64

        params = {
            "from": f"HOSPISOFT Resultados <{FROM_EMAIL}>",
            "to": [destinatario],
            "subject": "Resultado de examen médico - HOSPISOFT",
            "html": f"""
                <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
                    <h2 style="color: #059669;">Resultado de Examen Médico</h2>
                    <p>Hola <strong>{nombre}</strong>,</p>
                    <p>Su resultado de examen médico (documento: <strong>{documento}</strong>) 
                       ha sido registrado y se encuentra disponible.</p>
                    <p>Adjuntamos su resultado en formato PDF.</p>
                    <hr style="border: none; border-top: 1px solid #e5e7eb; margin: 20px 0;">
                    <p style="color: #9ca3af; font-size: 12px;">Equipo HOSPISOFT</p>
                </div>
            """,
            "text": f"Hola {nombre},\n\nSu resultado (doc: {documento}) está adjunto.\n\nSaludos,\nEquipo HOSPISOFT",
            "attachments": [{
                "filename": f"resultado_{documento}.pdf",
                "content": base64.b64encode(pdf_bytes).decode("utf-8"),
                "content_type": "application/pdf"
            }]
        }

        response = resend.Emails.send(params)
        
        if response.get("id"):
            logger.info(f"✅ Resultado enviado a {destinatario} (id: {response['id']})")
            return True
        else:
            logger.error(f"❌ Resend respondió sin ID: {response}")
            return False

    except Exception as e:
        logger.error(f"⚠️ Error Resend enviando resultado a {destinatario}: {e}")
        return False