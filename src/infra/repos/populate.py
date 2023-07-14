import random
import string
from sqlmodel import Session
from src.infra.configs.database import engine
from src.models.gem_models import *


def calculate_gem_price(gem: Gem, gem_p: GemProperties) -> any:
    """calculate."""
    price = 1000
    if gem.gem_type == "RUBY":
        price = 400
    elif gem.gem_type == "EMERALD":
        price = 650

    if gem_p.clarity == 1:
        price *= 0.75
    elif gem_p.clarity == 3:
        price *= 1.25
    elif gem_p.clarity == 4:
        price *= 1.5

    price = price * (gem_p.size**3)

    return price


def create_gem_props() -> GemProperties:
    """Test."""
    size = random.randint(3, 70) / 10
    color = random.choice(GemColor.list())
    clarity = random.randint(1, 4)

    gem_p = GemProperties(size=size, clarity=clarity, color=color)
    return gem_p


def create_gem(gem_p: GemProperties) -> Gem:
    """Test."""
    gem_type = random.choice(GemType.list())
    gem = Gem(price=1000, gem_properties_id=gem_p.id, gem_type=gem_type)
    price = calculate_gem_price(gem, gem_p)
    gem.price = price
    return gem


def create_gens_db():
    """Test."""
    gem_p = create_gem_props()

    with Session(engine) as session:
        session.add(gem_p)
        session.commit()

        gem = create_gem(gem_p)
        session.add(gem)
        session.commit()
