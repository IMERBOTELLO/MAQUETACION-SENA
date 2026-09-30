import os
import httpx
import base64
import logging

logger = logging.getLogger(__name__)

# Configuración desde variables de entorno
BREVO_API_KEY = os.getenv("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")
FROM_EMAIL = os.getenv("FROM_EMAIL", "hospisfot@gmail.com")
FROM_NAME = os.getenv("FROM_NAME", "HOSPISOFT")

BREVO_API_URL = "https://api.brevo.com/v3/smtp/email"

def _headers():
    return {
        "accept": "application/json",
        "api-key": BREVO_API_KEY,
        "content-type": "application/json"
    }


def enviar_correo(destinatario: str, nombre: str, contraseña: str) -> bool:
    if not BREVO_API_KEY:
        logger.warning("BREVO_API_KEY no configurado, omitiendo envío")
        return False
    
    try:
        payload = {
            "sender": {"name": FROM_NAME, "email": FROM_EMAIL},
            "to": [{"email": destinatario, "name": nombre}],
            "subject": "Bienvenido a HOSPISOFT",
            "htmlContent": f"""
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
                        le damos la bienvenida a nuestro sistema de hospitalización.
                    </p>
                    <hr style="border: none; border-top: 1px solid #e5e7eb; margin: 20px 0;">
                    <p style="color: #9ca3af; font-size: 12px;">Equipo HOSPISOFT</p>
                </div>
            """,
            "textContent": f"""Hola {nombre},

Su cuenta ha sido creada correctamente.

Credenciales de acceso:
Correo: {destinatario}
Contraseña: {contraseña}

Le damos la bienvenida a nuestro equipo de hospitalización.

Saludos,
Equipo HOSPISOFT"""
        }

        with httpx.Client(timeout=10) as client:
            resp = client.post(BREVO_API_URL, headers=_headers(), json=payload)

        if resp.status_code == 201:
            logger.info(f"✅ Correo enviado a {destinatario} (messageId: {resp.json().get('messageId')})")
            return True
        else:
            logger.error(f"❌ Brevo error {resp.status_code}: {resp.text}")
            return False

    except Exception as e:
        logger.error(f"⚠️ Error Brevo enviando a {destinatario}: {e}")
        return False


def enviar_resultado_correo(destinatario: str, nombre: str, documento: str, pdf_base64: str) -> bool:
    """Envía resultado médico con PDF adjunto vía Brevo API."""
    if not BREVO_API_KEY:
        logger.warning("BREVO_API_KEY no configurado, omitiendo envío de resultado")
        return False

    try:
        # Decodificar PDF a bytes
        if isinstance(pdf_base64, str):
            pdf_bytes = base64.b64decode(pdf_base64)
        else:
            pdf_bytes = pdf_base64

        # Brevo requiere adjuntos en base64
        pdf_b64 = base64.b64encode(pdf_bytes).decode("utf-8")

        payload = {
            "sender": {"name": f"{FROM_NAME} Resultados", "email": FROM_EMAIL},
            "to": [{"email": destinatario, "name": nombre}],
            "subject": f"Resultado de examen médico - HOSPISOFT ({documento})",
            "htmlContent": f"""
                <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
                    <h2 style="color: #059669;">Resultado de Examen Médico</h2>
                    <p>Hola <strong>{nombre}</strong>,</p>
                    <p>Su resultado de examen médico ha sido registrado 
                       (documento: <strong>{documento}</strong>) y se adjunta en PDF.</p>
                    <hr style="border: none; border-top: 1px solid #e5e7eb; margin: 20px 0;">
                    <p style="color: #9ca3af; font-size: 12px;">Equipo HOSPISOFT</p>
                </div>
            """,
            "textContent": f"Hola {nombre},\n\nAdjunto resultado (doc: {documento}).\n\nSaludos,\nEquipo HOSPISOFT",
            "attachment": [{
                "name": f"resultado_{documento}.pdf",
                "content": pdf_b64
            }]
        }

        with httpx.Client(timeout=15) as client:
            resp = client.post(BREVO_API_URL, headers=_headers(), json=payload)

        if resp.status_code == 201:
            logger.info(f"✅ Resultado enviado a {destinatario} (messageId: {resp.json().get('messageId')})")
            return True
        else:
            logger.error(f"❌ Brevo error adjunto {resp.status_code}: {resp.text}")
            return False

    except Exception as e:
        logger.error(f"⚠️ Error Brevo enviando resultado a {destinatario}: {e}")
        return False