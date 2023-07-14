from fastapi import APIRouter
from src.infra.repos.gem_repo import GemRepo
from sqlmodel import Session
from typing import List
from src.models.gem_models import Gem
from .models.gems import GemResponse

router = APIRouter(prefix="/gems")


@router.delete("/{id}", status_code=204)
def delete(id: int):
    """Delete Gems."""
    repo = GemRepo(Session)
    gem = repo.select_gem(id)
    repo.delete(gem)
