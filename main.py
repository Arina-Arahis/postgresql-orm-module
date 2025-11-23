#!/usr/bin/env python3
from app.database import db_manager
from app.crud import UserCRUD
import time

def main():
    print("=== Демонстрация модуля работы с PostgreSQL ===")
    
    # Создание таблиц
    db_manager.create_tables()
    print("Таблицы созданы")
    
    # Количество записей
    count = UserCRUD.get_user_count()
    print(f"Количество записей в таблице: {count}")
    
    # Добавление записи
    new_user = UserCRUD.add_user("Demo User", "active")
    print(f"Добавлена запись: ID={new_user.id}, Name={new_user.name}, Status={new_user.status}")
    
    # Пагинация - страница 1, 5 записей
    print("\nПагинация - Страница 1 (5 записей):")
    users = UserCRUD.get_users_paginated(page=1, page_size=5)
    for user in users:
        print(f"  ID: {user.id}, Name: {user.name}, Status: {user.status}")
    
    # Пагинация - страница 2, 5 записей
    print("\nПагинация - Страница 2 (5 записей):")
    users = UserCRUD.get_users_paginated(page=2, page_size=5)
    for user in users:
        print(f"  ID: {user.id}, Name: {user.name}, Status: {user.status}")
    
    # Удаление записи
    if UserCRUD.delete_user(new_user.id):
        print(f"\nЗапись с ID {new_user.id} удалена")
    
    # Финальное количество
    final_count = UserCRUD.get_user_count()
    print(f"\nФинальное количество записей: {final_count}")

if __name__ == "__main__":
    main()