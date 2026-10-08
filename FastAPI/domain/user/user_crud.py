from sqlalchemy.orm import Session
from domain.user.user_schema import UserCreate
from models import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes = ["bcrypt"], deprecated = "auto")

# 새 회원 저장
def create_user(db: Session, user_create: UserCreate):
    db_user = User(username = user_create.username,
                   password = pwd_context.hash(user_create.password1),
                   email = user_create.email)
    db.add(db_user)
    db.commit()

# 중복값 조회
def get_existing_user(db: Session, user_create: UserCreate):
    return db.query(User).filter(
        (User.username == user_create.username) |
        (User.email == user_create.email)
    ).first()

# 사용자명으로 사용자 모델 객체를 리턴
def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()