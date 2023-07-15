from src.infra.configs.database import engine
from src.models.user_model import User, UserInput
from sqlmodel import Session, select
from typing import List


class UserRepo:
    """User repository."""

    def __init__(self, session: Session) -> None:
        """Construct."""
        self._session = session

    def select_user(self, user_name: str) -> User:
        """Select a by name."""
        with self._session(engine) as session_:
            stmt = select(User).where(User.username == user_name)
            result = session_.exec(stmt)
            return result.first()

    def create(self, user: UserInput) -> UserInput:
        """Create a User."""
        user = User(**user.dict())
        with self._session(engine) as session_:
            session_.add(user)
            session_.commit()

    def delete(self, user: UserInput) -> User:
        """Delete a User."""
        user = User(**user.dict())
        with self._session(engine) as session_:
            session_.delete(user)
            session_.commit()
        return user
