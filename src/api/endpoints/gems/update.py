from fastapi import APIRouter
from src.infra.repos.gem_repo import GemRepo
from sqlmodel import Session
from typing import List
from src.models.gem_models import Gem
from .models.gems import GemResponse

router = APIRouter(prefix="/gems")


@router.put("/{id}", status_code=200, response_model=GemResponse, tags=["Gem"])
def create(id: int, new_gem: Gem) -> GemResponse:
    """Create Gems."""
    repo = GemRepo(Session)
    old_gem = repo.select_gem(id)
    repo.delete(old_gem)

    r = GemResponse(gem=new_gem, status="Updated")
    repo.create(new_gem)
    return r
