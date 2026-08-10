from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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
        
        server = SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(correo_emisor, contraseña_emisor)
        
        server.send_message(mensaje)
        
        server.quit()
        print("Correo enviado exitosamente")
        
    except Exception as e:
        print(f"Error enviando correo: {e}")
        raise