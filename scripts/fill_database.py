
#!/usr/bin/env python3
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

print(" Начинаем заполнение базы...")

try:
    from app.database import db_manager
    from app.crud import UserCRUD
    print(" Модули загружены")
    

    print(" Создаем таблицы...")
    db_manager.create_tables()
    

    count = UserCRUD.get_user_count()
    print(f" Текущее количество записей: {count}")
    
    if count < 100000:
        print(" Добавляем 100000 записей...")
        UserCRUD.bulk_create_users(100000)
    else:
        print(" Уже достаточно записей")
        

    final_count = UserCRUD.get_user_count()
    print(f" Финальное количество: {final_count}")
    
except Exception as e:
    print(f" Ошибка: {e}")
    import traceback
    traceback.print_exc()
