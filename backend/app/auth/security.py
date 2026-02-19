import os
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import jwt
from typing import Any, Dict

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
secret_key = os.getenv("JWT_SECRET")
if not secret_key:
    raise RuntimeError("JWT_SECRET não definido")
algorithm = os.getenv("JWT_ALG", "HS256")
access_token_expire_min = int(os.getenv("ACCESS_TOKEN_EXPIRE_MIN", 60))

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

def create_access_token(subject: str) -> str:
    if not secret_key:
        raise RuntimeError("JWT_SECRET não definido")
    expire = datetime.now(timezone.utc) + timedelta(minutes=access_token_expire_min)
    payload: Dict[str, Any] = {"sub": subject, "exp": int(expire.timestamp())}
    return jwt.encode(payload, secret_key, algorithm=algorithm)