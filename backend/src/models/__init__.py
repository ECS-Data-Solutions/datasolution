from sqlalchemy.orm import declarative_base
from src.plugins import dto_factory

# Import Models
from src.models.User import User
# End Import Models


__all__ = [
    "Base",
    "dto_factory"
]

Base = declarative_base()
