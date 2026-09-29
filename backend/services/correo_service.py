from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import base64

def enviar_correo(destinatario, nombre, contraseña):

    try:
        
        correo_emisor = "hospisfot@gmail.com"
        contraseña_emisor = "kvem rnvo sfnt xkbb"
        
        asunto = "Bienvenido a HOSPISOFT"
        
        cuerpo = f"""
    hola {nombre},

    su cuenta a sido creada logueada correctamente

    puede ingresar a HOSPISOFT con:

    correo:
    {destinatario}

    contraseña:
    {contraseña}

    Le recomendamos entrar a nuestro sistema de atencion

    saludos.
    Equipo HOSPISOFT
    """

        mensaje = MIMEMultipart()
        mensaje['From'] = correo_emisor
        mensaje['To'] = destinatario
        mensaje['Subject'] = asunto
        
        mensaje.attach(MIMEText(cuerpo, 'plain'))
        
        server = SMTP_SSL('smtp.gmail.com', 465, timeout=10)
        server.login(correo_emisor, contraseña_emisor)
        
        server.send_message(mensaje)
        
        server.quit()
        print("Correo enviado exitosamente")
        
    except Exception as e:
        print(f"Error enviando correo: {e}")
        raise
    
    
def enviar_resultado_correo(destinatario, nombre, documento, pdf):
    
    try:
        
        correo_emisor = "hospisfot@gmail.com"
        contraseña_emisor = "kvem rnvo sfnt xkbb"
        
        
        # PREPARARA EL PDF EN BASE64
        if isinstance(pdf, str):
            
            # si viene como base64 en texto
            
            pdf_bytes = base64.b64decode(pdf)
            
        elif isinstance(pdf, bytes):
            
            # verificamos si ya son bytes reales en pdf
            
            if pdf.startswith(b'%PDF'):
                
                pdf_bytes = pdf
                
            else:
                
                # probablemente son bytes que contiene base64
                pdf_bytes = base64.b64decode(pdf)
                
        else:
            
            raise Exception("PDF no reconocido")
        
        asunto = "Resultado de examen medico - HOSPISOFT"
        
        cuerpo = f"""
Hola {nombre},

Su resultado de examen medico ha sido registrado con el documento ya se encuentra disponible en HOSPISOFT:

Datos del paciente:

Nombre: {nombre}
Documento: {documento}

Adjuntamos su resultado en formato PDF:

Saludos,
Equipo HOSPISOFT
"""

        mensaje = MIMEMultipart()
        
        mensaje['From'] = correo_emisor
        mensaje['To'] = destinatario
        mensaje['Subject'] = asunto
        
        mensaje.attach(
            MIMEText(cuerpo, 'plain')
        )
        
        # crear archivo adjunto
        archivo_pdf = MIMEApplication(
            pdf_bytes,
            _subtype = "pdf"
        )
        
        archivo_pdf.add_header(
            "Content-Disposition",
            "attachment",
            filename=f"resultado_{documento}.pdf"
        )
        
        mensaje.attach(archivo_pdf)
        
        # conectar con gmail
        
        server = SMTP_SSL("smtp.gmail.com", 465, timeout=10)
        server.login(
            correo_emisor, 
            contraseña_emisor
        )
        
        server.send_message(mensaje)
        
        server.quit()
        
        print("Correo con resultado enviado exitosamente")
        
    except Exception as e:
        print(f"Error enviando correo con resultado: {e}")
        
        raise