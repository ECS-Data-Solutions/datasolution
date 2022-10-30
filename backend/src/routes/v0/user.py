from starlite import Controller, get, post
from src.models.User import User, CreateUserDTO
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class UserController(Controller):
    path = "/user"

    @get()
    async def get_user_by_id(
            self,
            user_id: int,
            db_session: AsyncSession
    ) -> dict:
        user = (await db_session.scalar(select(User).where(User.id == user_id))).one_or_none()
        return {
            "id": user.id,
            "name": user.name,
            "fullname": user.fullname,
        }

    @post()
    async def create_user(
            self,
            data: CreateUserDTO,
            db_session: AsyncSession
    ) -> dict:
        user = User(**data.dict())
        db_session.add(user)
        await db_session.commit()
        return {
            "id": user.id,
            "name": user.name,
            "fullname": user.fullname,
        }
