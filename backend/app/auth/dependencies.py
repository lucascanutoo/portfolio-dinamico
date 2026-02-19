from fastapi.security import OAuth2PasswordBearer

oath2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

def get_current_user(token: Depends(oath2_scheme), db: Depends(get_db)):
    