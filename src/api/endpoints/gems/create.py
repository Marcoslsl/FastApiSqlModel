from fastapi import APIRouter
from src.infra.repos.gem_repo import GemRepo
from sqlmodel import Session
from typing import List
from src.models.gem_models import Gem, GemInputCreat, GemProperties
from .models.gems import GemResponse
from fastapi import Depends
from src.auth.auth import AuthHandler

router = APIRouter(prefix="/gems")


@router.post("", status_code=201, response_model=GemResponse, tags=["Gem"])
def create(
    gem_p: GemProperties,
    gem: GemInputCreat,
    user: any = Depends(AuthHandler().auth_wrapper),
) -> GemResponse:
    """Create Gems."""
    GemRepo(Session).create(gem_p)
    gem = Gem(**gem.dict())
    gem_ = gem.copy()
    GemRepo(Session).create(gem)
    r = GemResponse(gem=gem_, status="Created")
    return r
