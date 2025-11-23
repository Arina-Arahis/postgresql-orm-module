import os
from dataclasses import dataclass

@dataclass
class DatabaseConfig:
    host: str = "localhost"
    port: int = 5432
    database: str = "test_db"
    username: str = "test_user1"
    password: str = "test_password"

    @property
    def database_url(self):
        return f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"

# Создаем экземпляр конфигурации - ЭТА СТРОКА ДОЛЖНА БЫТЬ!
db_config = DatabaseConfig()