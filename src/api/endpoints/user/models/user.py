from pydantic import BaseModel


class UserLogin(BaseModel):
    """Login model."""

    username: str
    password: str


class UserLoginResponse(BaseModel):
    """Login model."""

    username: str
    access_token: str
