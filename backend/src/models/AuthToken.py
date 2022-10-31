from src.models import Base, dto_factory
from sqlalchemy import Column, Float, Integer, String, DateTime
import datetime

__all__ = ["AuthToken"]

class AuthToken(Base):
    __tablename__ = "authtoken"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    token = Column(String)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self) -> dict:
        return {
            "id": self.id,
            "user_id": self.user_id,
            "token": self.token,
            "created_date": self.created_date,
        }


CreateAuthTokenDTO = dto_factory("CreateUserDTO", AuthToken, exclude=["id", "created_date"])
