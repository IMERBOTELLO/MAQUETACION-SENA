from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

DATABASES_URL = (
    f"mysql+pymysql://{os.getenv('avnadmin')}:"
    f"{os.getenv('AVNS_csYXxhJPBa_gGeiLAzC')}@"
    f"{os.getenv('mysql-13ad6284-imerantoniobotellopaez-445a.h.aivencloud.com')}:"
    f"{os.getenv('19205')}/"
    f"{os.getenv('ATENCION_MEDICA')}"
)

engine = create_engine(DATABASES_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)