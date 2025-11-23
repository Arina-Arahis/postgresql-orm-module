from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base
from config import db_config


engine = create_engine(db_config.database_url)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_tables():
    Base.metadata.create_all(bind=engine)


def get_session():
    return SessionLocal()


class DatabaseManager:
    def __init__(self):
        self.engine = engine
        self.SessionLocal = SessionLocal
    
    def create_tables(self):
        create_tables()
    
    def get_session(self):
        return get_session()


db_manager = DatabaseManager()
