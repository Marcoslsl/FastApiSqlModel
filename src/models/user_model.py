from pydantic import validator, EmailStr
from typing import Optional
from datetime import date
from sqlmodel import SQLModel, Field, Relationship


class User(SQLModel, table=True):
    """User."""

    id: Optional[int] = Field(primary_key=True)
    username: str = Field(index=True)
    password: str = Field(max_length=256, min_length=6)
    email: EmailStr
    created_at: date = date.today()
    is_seller: bool = False


class UserInput(SQLModel):
    """User input."""

    username: str
    password: str = Field(max_length=256, min_length=6)
    password2: str
    email: EmailStr
    is_seller: bool = False

    @validator("password2")
    def senhas_iguais(cls, v, values):
        """Validate."""
        if v == values["password1"]:
            return v
        else:
            raise ValueError("passwords don't match")
