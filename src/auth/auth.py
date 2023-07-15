from fastapi import Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from passlib.context import CryptContext
import datetime
import jwt
from src.infra.repos.user_repo import UserRepo
from sqlmodel import Session


class AuthHandler:
    """Auth handler."""

    pwd_context = CryptContext(schemes=["bcrypt"])
    secret = "supersecret"

    def get_password_hash(self, password):
        """Get password hash."""
        return self.pwd_context.hash(password)

    def verify_password(self, pwd, hashed_pwd):
        """Verify password."""
        return self.pwd_context.verify(pwd, hashed_pwd)

    def encode_token(self, username: str):
        """Get token."""
        payload = {
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=6),
            "iat": datetime.datetime.utcnow(),
            "sub": username,
        }
        return jwt.encode(payload, self.secret, algorithm="HS256")

    def decode_token(self, token):
        """Decode token."""
        try:
            payload = jwt.decode(token, self.secret, algorithms=["HS256"])
            return payload["sub"]
        except Exception as e:
            raise e

    def auth_wrapper(
        self, auth: HTTPAuthorizationCredentials = Security(HTTPBearer())
    ):
        """Validate de token passed."""
        return self.decode_token(auth.credentials)

    def get_current_user(
        self, auth: HTTPAuthorizationCredentials = Security(HTTPBearer())
    ):
        """Get current user."""
        username = self.decode_token(auth.credentials)
        if username is None:
            raise Exception("ERROR")

        user = UserRepo(Session).select_user(username)
        if user is None:
            raise Exception("ERRO")

        return user
