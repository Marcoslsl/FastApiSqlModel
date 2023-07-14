from src.infra.configs.database import engine
from src.models.gem_models import Gem, GemProperties
from sqlmodel import Session, select
from typing import List


class GemRepo:
    """Gem repository."""

    def __init__(self, session: Session) -> None:
        """Construct."""
        self._session = session

    def select_all_gems(self) -> List[Gem]:
        """Select all gems."""
        with self._session(engine) as session_:
            stmt = select(Gem)
            result = session_.exec(stmt)
            return result.all()

    def select_gem(self, gem_id: int) -> List[Gem]:
        """Select a gem by id."""
        with self._session(engine) as session_:
            stmt = select(Gem).where(Gem.id == gem_id)
            result = session_.exec(stmt)
            return result.first()

    def create(self, gem: Gem) -> Gem:
        """Create a gem."""
        with self._session(engine) as session_:
            session_.add(gem)
            session_.commit()

    def delete(self, gem: Gem) -> Gem:
        """Delete a gem."""
        with self._session(engine) as session_:
            session_.delete(gem)
            session_.commit()
        return gem
