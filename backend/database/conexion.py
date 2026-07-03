from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# URL DE CONEXION HACIA MYSQL
DATABASES_URL = "mysql+pymysql://HOSPISOFT:12345@127.0.0.1:3306/atencion_medica"

# motor de conexion
engine = create_engine(DATABASES_URL)

#FABRICA DE SESIONES
SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine
)