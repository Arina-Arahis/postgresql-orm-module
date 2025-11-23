import unittest
from app.database import db_manager
from app.crud import UserCRUD

class TestDatabase(unittest.TestCase):
    def setUp(self):
        db_manager.create_tables()
    
    def test_add_user(self):
        user = UserCRUD.add_user("Test User", "active")
        self.assertIsNotNone(user.id)
        self.assertEqual(user.name, "Test User")
    
    def test_pagination(self):
        users = UserCRUD.get_users_paginated(page=1, page_size=5)
        self.assertIsInstance(users, list)
    
    def test_count(self):
        count = UserCRUD.get_user_count()
        self.assertIsInstance(count, int)

if __name__ == "__main__":
    unittest.main()