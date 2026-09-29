import os
import httpx
import base64
import logging

logger = logging.getLogger(__name__)

# Configuración desde variables de entorno
MAILGUN_API_KEY = os.getenv("7543e985-83d05613")
MAILGUN_DOMAIN = os.getenv("hospisoft.com")
FROM_EMAIL = os.getenv("FROM_EMAIL", "hospsoft@gmail.com")

async def enviar_correo(destinatario: str, nombre: str, contraseña: str) -> bool:
    if not MAILGUN_API_KEY or not MAILGUN_DOMAIN:
        logger.warning("MAILGUN_API_KEY o MAILGUN_DOMAIN no configurado, omitiendo envío")
        return False
    
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
                auth=("api", MAILGUN_API_KEY),
                data={
                    "from": f"HOSPISOFT <{FROM_EMAIL}>",
                    "to": destinatario,
                    "subject": "Bienvenido a HOSPISOFT",
                    "text": f"Hola {nombre},\n\nCredenciales:\nCorreo: {destinatario}\nContraseña: {contraseña}\n\nSaludos,\nEquipo HOSPISOFT",
                    "html": f"""<h2>Bienvenido a HOSPISOFT</h2>
                        <p>Hola <strong>{nombre}</strong>,</p>
                        <p>Credenciales:<br>Correo: {destinatario}<br>Contraseña: {contraseña}</p>"""
                },
                timeout=10
            )
        return resp.status_code == 200
    except Exception as e:
        logger.error(f"Mailgun error: {e}")
        return False
    
async def enviar_resultado_correo(destinatario: str, nombre: str, documento: str, pdf_base64: str) -> bool:
    if not MAILGUN_API_KEY or not MAILGUN_DOMAIN:
        return False
    
    try:
        pdf_bytes = base64.b64decode(pdf_base64) if isinstance(pdf_base64, str) else pdf_base64
        
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
                auth=("api", MAILGUN_API_KEY),
                data={
                    "from": f"HOSPISOFT Resultados <{FROM_EMAIL}>",
                    "to": destinatario,
                    "subject": f"Resultado examen médico - {documento}",
                    "text": f"Hola {nombre},\n\nAdjunto resultado (doc: {documento}).\n\nSaludos,\nEquipo HOSPISOFT",
                    "html": f"<p>Hola {nombre},</p><p>Adjunto resultado (doc: <strong>{documento}</strong>).</p>"
                },
                files={
                    "attachment": (f"resultado_{documento}.pdf", pdf_bytes, "application/pdf")
                },
                timeout=15
            )
        return resp.status_code == 200
    except Exception as e:
        logger.error(f"Mailgun error: {e}")
        return False
                    