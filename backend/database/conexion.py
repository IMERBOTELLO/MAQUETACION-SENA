from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASES_URL = "mysql+pymysql://HOSPISOFT:12345@127.0.0.1:3306/atencion_medica"

engine = create_engine(DATABASES_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)