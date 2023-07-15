from fastapi import APIRouter
from src.infra.repos.gem_repo import GemRepo
from sqlmodel import Session
from typing import List
from src.models.gem_models import Gem

router = APIRouter(prefix="/gems")


@router.get("", status_code=200, response_model=List[Gem], tags=["Gem"])
def gems() -> List[Gem]:
    """List Gems."""
    gems = GemRepo(Session).select_all_gems()
    return gems


@router.get("/{gem_id}", status_code=200, response_model=Gem, tags=["Gem"])
def gems(gem_id: int) -> Gem:
    """Get gem by id."""
    gems = GemRepo(Session).select_gem(gem_id)
    return gems
