from sqlmodel import SQLModel, Field
from enum import Enum
from typing import Optional


class GemClarity(Enum):
    """Gem clarity."""

    SI = 1
    VS = 2
    VVS = 3
    FL = 4


class GemColor(Enum):
    """Gem color."""

    D = "D"
    E = "E"
    G = "G"
    F = "F"
    H = "H"
    i = "I"


class GemType(Enum):
    """Gem types."""

    DIAMOND = "DIAMOND"
    EMERALD = "EMERALD"
    RUBY = "RUBY"


class GemProperties(Enum):
    """Gem properties."""

    id: Field(primary_key=True)
    size: float = 1
    clarity: Optional[GemClarity] = None
    color: Optional[GemColor] = None


class Gem(SQLModel, table=True):
    """Gem."""

    id: Field(primary_key=True)
    price: float
    available: bool = True
    gen_type: GemType = GemType.DIAMOND

    gem_properties: Optional[int] = Field(
        default=None, foreign_key="gemproperties.id"
    )
