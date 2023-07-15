from fastapi import APIRouter, Depends
from src.infra.repos.user_repo import UserRepo
from sqlmodel import Session
from typing import List
from src.models.user_model import UserInput, User
from .models.user import UserLoginResponse, UserLogin
from src.auth.auth import AuthHandler

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("", status_code=201)
def create(user: UserInput):
    """Create User."""
    hashed_pwd = AuthHandler().get_password_hash(user.password)
    user.password = hashed_pwd

    user_ = user.copy()
    UserRepo(Session).create(user_)
    return {"msg": "Created"}


@router.post("/login", status_code=201)
def login(user: UserLogin):
    """login."""
    user_response = UserRepo(Session).select_user(user.username)

    verify = AuthHandler().verify_password(
        user.password, user_response.password
    )

    if verify:
        token = AuthHandler().encode_token(user.username)
        return UserLoginResponse(username=user.username, access_token=token)
    else:
        raise ValueError("ERROR.")


@router.get("/user/me")
def me(user: User = Depends(AuthHandler().get_current_user)):
    return user.username
