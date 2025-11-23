
import sys
import os
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.crud import UserCRUD

def benchmark_pagination():
    print("Тестирование производительности пагинации:")
    
    test_cases = [
        (1, 10),
        (100, 20),
        (1000, 50),
        (5000, 100)
    ]
    
    for page, page_size in test_cases:
        start_time = time.time()
        users = UserCRUD.get_users_paginated(page=page, page_size=page_size)
        end_time = time.time()
        
        print(f"Страница {page}, размер {page_size}: {end_time - start_time:.4f} сек, записей: {len(users)}")

if __name__ == "__main__":
    benchmark_pagination()