from sqlalchemy.exc import SQLAlchemyError
from app.database import db_manager
from app.models import User
import random

class UserCRUD:
    @staticmethod
    def get_user_count():
        """Получение количества строк в таблице"""
        session = db_manager.get_session()
        try:
            return session.query(User).count()
        finally:
            session.close()
    
    @staticmethod
    def add_user(name: str, status: str):
        """Добавление новой записи"""
        session = db_manager.get_session()
        try:
            user = User(name=name, status=status)
            session.add(user)
            session.commit()
            session.refresh(user)
            return user
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
    @staticmethod
    def get_users_paginated(page: int, page_size: int):
        """Получение записей с пагинацией"""
        session = db_manager.get_session()
        try:
            offset = (page - 1) * page_size
            users = session.query(User).offset(offset).limit(page_size).all()
            return users
        finally:
            session.close()
    
    @staticmethod
    def delete_user(user_id: int):
        """Удаление записи по ID"""
        session = db_manager.get_session()
        try:
            user = session.query(User).filter(User.id == user_id).first()
            if user:
                session.delete(user)
                session.commit()
                return True
            return False
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
    @staticmethod
    def bulk_create_users(count: int = 100000):
        """Создание 100k+ записей"""
        session = db_manager.get_session()
        try:
            statuses = ['active', 'inactive', 'pending', 'blocked']
            batch_size = 1000
            
            for i in range(0, count, batch_size):
                current_batch = min(batch_size, count - i)
                users = []
                
                for j in range(current_batch):
                    user = User(
                        name=f"User_{i + j + 1}",
                        status=random.choice(statuses)
                    )
                    users.append(user)
                
                session.bulk_save_objects(users)
                session.commit()
                
                if (i + current_batch) % 10000 == 0:
                    print(f"Добавлено {i + current_batch} записей")
            
            print(f"Создано {count} записей")
            
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()