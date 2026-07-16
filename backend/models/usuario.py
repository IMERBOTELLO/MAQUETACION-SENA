from sqlalchemy import Column, Integer, String, Enum
from backend.database.base import Base

class Usuario(Base):
    __tablename__ = 'USUARIO'
    
    id_usuario = Column(Integer, primary_key = True, autoincrement = True)
    correo = Column(String(150), unique = True, nullable = False)
    contraseña = Column(String(150), nullable = False)
    rol = Column(Enum('RECEPCIONISTA', 'MEDICO', 'LABORATORIO', 'PACIENTE', 'ADMINISTRADOR'), nullable = False)

