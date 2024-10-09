from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config.config import DATABASE_URL

engine = create_engine(DATABASE_URL, connect_args={"options": "-c client_encoding=utf8"})
# Базовый класс для моделей
Base = declarative_base()
# Получаем строку подключения из config.config.py или переменной окружения

# Создаём фабрику сессий для работы с базой данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Функция для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
