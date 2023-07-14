from pydantic import BaseModel
from src.models.gem_models import Gem


class GemResponse(BaseModel):
    """Gem response model."""

    gem: Gem
    status: str
