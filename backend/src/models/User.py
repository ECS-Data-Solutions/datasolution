from src.models import Base, dto_factory
from sqlalchemy import Column, Float, Integer, String

__all__ = ["User"]

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    email = Column(String)
    password = Column(String)

    def __repr__(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "fullname": self.fullname,
            "email": self.email,
            "password": self.password,
        }


CreateUserDTO = dto_factory("CreateUserDTO", User, exclude=["id"])
