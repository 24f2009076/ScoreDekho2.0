from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from controllers.database import engine, get_db
from controllers.models import Base, User
from controllers.schemas import UserResponse
from controllers.auth import router as auth_router, oauth2_scheme, decode_token, get_current_user
from controllers.seed import seed_users

Base.metadata.create_all(bind=engine)
seed_users()

app = FastAPI(title="ScoreDekho API")

app.include_router(auth_router)


@app.get("/")
def home():
    return {"message": "Welcome to the ScoreDekho API! Explore the endpoints to manage teams and players."}


@app.get("/me", response_model=UserResponse)
def me(current_user : User = Depends(get_current_user)):
    return current_user
