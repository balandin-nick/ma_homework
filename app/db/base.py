from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.settings.db import service_database_settings


__all__ = [
    "engine",
    "SessionLocal",
    "BaseDBMetaModel",
    "get_session",
]


engine = create_engine(url=service_database_settings.postgresql_url, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
BaseDBMetaModel = declarative_base()


def get_session() -> Generator[SessionLocal, None, None]:
    session = SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()
