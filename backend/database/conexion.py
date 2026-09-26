from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

DATABASES_URL = (
    "mysql+pymysql://avnadmin:"
    "AVNS_csYXxhJPBa_gGeiLAzC@"
    "mysql-13ad6284-imerantoniobotellopaez-445a.h.aivencloud.com:"
    "19205/"
    "ATENCION_MEDICA"
)

engine = create_engine(DATABASES_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)