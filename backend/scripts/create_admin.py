import os
from sqlalchemy import select
from app.db.database import SessionLocal
from app.models import User
from app.auth.security import get_password_hash

def create_admin_user():
    db = SessionLocal()
    admin_user = os.getenv("ADMIN_USER")
    admin_pass = os.getenv("ADMIN_PASS")
    if not admin_user or not admin_pass:
        print("ADMIN_USER ou ADMIN_PASS não definidos no .env")
        return
    existing_user = db.execute(select(User).where(User.username == admin_user)).scalar_one_or_none()
    if not existing_user:
        new_user = User(username=admin_user, hashed_password=get_password_hash(admin_pass), is_admin=True)
        db.add(new_user)
        db.commit()
        print("Admin user criado com sucesso.")
    else:
        print("Admin user já existe.")
    
    db.close()

create_admin_user()