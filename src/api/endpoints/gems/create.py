from fastapi import APIRouter
from src.infra.repos.gem_repo import GemRepo
from sqlmodel import Session
from typing import List
from src.models.gem_models import Gem
from .models.gems import GemResponse

router = APIRouter(prefix="/gems")


@router.post("", status_code=201, response_model=GemResponse)
def create(gem: Gem) -> GemResponse:
    """Create Gems."""
    gem_ = gem.copy()
    GemRepo(Session).create(gem)
    r = GemResponse(gem=gem_, status="Created")
    return r
