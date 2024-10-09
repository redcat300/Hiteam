from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# print(f"Loaded .env file from: {env_path.resolve()}")
# print(f"DATABASE_URL: {os.getenv('DATABASE_URL')}")
