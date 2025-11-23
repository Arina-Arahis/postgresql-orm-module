from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    status = Column(String(50), index=True)
    
    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', status='{self.status}')>"