from starlite import Controller, get, post
from src.models.User import User, CreateUserDTO
from sqlalchemy.orm import Session
from sqlalchemy import select


class UserController(Controller):
    path = "/user"

    @get()
    def get_user_by_id(
            self,
            user_id: int,
            db_session: Session
    ) -> dict:
        user = db_session.scalar(select(User).where(User.id == user_id)).one_or_none()
        return {
            "id": user.id,
            "name": user.name,
            "fullname": user.fullname,
        }

    @post()
    def create_user(
            self,
            data: CreateUserDTO,
            db_session: Session
    ) -> dict:
        user = User(**data.dict())
        db_session.add(user)
        db_session.commit()
        return {
            "id": user.id,
            "name": user.name,
            "fullname": user.fullname,
        }
