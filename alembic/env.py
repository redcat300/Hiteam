import os
import sys
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig
from alembic import context
from app.db.database import Base
from app.models.models import User, Channel, TextChat, VoiceRoom
from dotenv import load_dotenv
from pathlib import Path

# Добавляем корневую директорию в sys.path
sys.path.append(str(Path('.').resolve()))

# Задаем путь к .env
env_path = Path('.') / '.env'
print(f"Loading .env file from: {env_path.resolve()}")
load_dotenv(dotenv_path=env_path)

# Проверяем значение переменной DATABASE_URL
database_url = os.getenv("DATABASE_URL")
print(f"DATABASE_URL: {database_url}")
if not database_url:
    raise ValueError("DATABASE_URL is not set")

# Alembic
from alembic import context
from app.db.database import Base  # Теперь Python должен найти этот модуль

context.config.set_main_option("sqlalchemy.url", database_url)

target_metadata = Base.metadata

# Функции для миграций
def run_migrations_offline():
    url = context.config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        context.config.get_section(context.config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()