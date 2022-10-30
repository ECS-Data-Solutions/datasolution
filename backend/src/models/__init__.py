from sqlalchemy.orm import declarative_base
from src.plugins import dto_factory

__all__ = [
    "Base",
    "dto_factory"
]

Base = declarative_base()
