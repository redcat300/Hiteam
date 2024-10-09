from dotenv import load_dotenv
import os
from urllib.parse import quote_plus

# Загрузка переменных окружения
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '..', '.env'))

# Кодирование переменных окружения для безопасности URL
DB_USER = quote_plus(os.getenv("DB_USER", ""))
DB_PASS = quote_plus(os.getenv("DB_PASS", ""))
DB_HOST = os.getenv("DB_HOST", "")
DB_PORT = os.getenv("DB_PORT", 5432)
DB_NAME = os.getenv("DB_NAME", "")
DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

# Проверка на наличие всех необходимых параметров
if not all([DB_USER, DB_PASS, DB_HOST, DB_NAME]):
    raise ValueError("One or more database connection parameters are missing.")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# print(f"DB_USER: {DB_USER}")
# print(f"DB_PASS: {DB_PASS}")
# print(f"DB_HOST: {DB_HOST}")
# print(f"DB_PORT: {DB_PORT}")
# print(f"DB_NAME: {DB_NAME}")

# Сборка строки подключения с закодированными переменными

# print(f"DATABASE_URL: {DATABASE_URL}")

