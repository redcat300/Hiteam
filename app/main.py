from fastapi import FastAPI
from app.auth.auth import router as auth_router  # Убедись, что правильно импортируешь маршруты
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Или укажи конкретные источники, если необходимо
    allow_credentials=True,
    allow_methods=["*"],  # Или укажи конкретные методы
    allow_headers=["*"],  # Или укажи конкретные заголовки
)
# Подключение маршрутов для аутентификации
app.include_router(auth_router, prefix="/auth", tags=["auth"])

@app.get("/")
async def read_root():
    return {"Hello": "World"}
