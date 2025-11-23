from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base
from config import db_config

# Создаем движок
engine = create_engine(db_config.database_url)

# Создаем фабрику сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создаем таблицы
def create_tables():
    Base.metadata.create_all(bind=engine)

# Получаем сессию
def get_session():
    return SessionLocal()

# Создаем менеджер для обратной совместимости
class DatabaseManager:
    def __init__(self):
        self.engine = engine
        self.SessionLocal = SessionLocal
    
    def create_tables(self):
        create_tables()
    
    def get_session(self):
        return get_session()

# Экземпляр менеджера
db_manager = DatabaseManager()