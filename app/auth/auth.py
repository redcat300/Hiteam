from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.db.database import get_db  # Импортируй метод получения сессии БД
from app.auth.schemas import UserRegister, UserLogin, UserOut  # Импортируй схемы
from app.auth.utils import hash_password, create_access_token, verify_password  # Импортируй функции из utils
from app.models.models import User  # Импортируй модель User

router = APIRouter()

@router.post("/token")
def login(user: UserLogin, db: Session = Depends(get_db)):
    # Проверка существующего пользователя
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    # Создание JWT
    access_token = create_access_token(data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user: UserRegister, db: Session = Depends(get_db)):
    # Проверка существования пользователя
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    # Хэшируем пароль перед сохранением
    hashed_password = hash_password(user.password)

    # Создаем нового пользователя
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user