from fastapi import FastAPI
from app.auth.auth import router as auth_router  # Убедись, что правильно импортируешь маршруты

app = FastAPI()

# Подключение маршрутов для аутентификации
app.include_router(auth_router, prefix="/auth", tags=["auth"])

@app.get("/")
async def read_root():
    return {"Hello": "World"}
