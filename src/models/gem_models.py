from sqlmodel import SQLModel, Field
from enum import Enum, IntEnum
from typing import Optional
from sqlmodel import Relationship


class Enum(Enum):
    """Enum."""

    @classmethod
    def list(cls):
        """List."""
        return list(map(lambda x: x.value, cls))


class GemClarity(IntEnum):
    """Gem clarity."""

    SI = 1
    VS = 2
    VVS = 3
    FL = 4


class GemColor(str, Enum):
    """Gem color."""

    D = "D"
    E = "E"
    G = "G"
    F = "F"
    H = "H"
    i = "I"


class GemType(str, Enum):
    """Gem types."""

    DIAMOND = "DIAMOND"
    EMERALD = "EMERALD"
    RUBY = "RUBY"


class GemProperties(SQLModel, table=True):
    """Gem properties."""

    id: Optional[int] = Field(primary_key=True)
    size: float = 1
    clarity: Optional[GemClarity] = None
    color: Optional[GemColor] = None
    gems: Optional["Gem"] = Relationship(back_populates="gem_properties")


class Gem(SQLModel, table=True):
    """Gem."""

    id: Optional[int] = Field(primary_key=True)
    price: float
    available: bool = True
    gem_type: GemType = GemType.DIAMOND

    gem_properties_id: Optional[int] = Field(
        default=None, foreign_key="gemproperties.id"
    )
    gem_properties: Optional[GemProperties] = Relationship(
        back_populates="gems"
    )
