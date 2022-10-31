from starlite import Controller, get, post, delete, NotFoundException, Parameter
from src.models.User import User, CreateUserDTO
from src.models.AuthToken import AuthToken
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.lib.authtoken import create_auth_token
from src.lib.encrypt import encrypt_password


class UserController(Controller):
    path = "/user"

    @get()
    async def get_user_by_id(
            self,
            user_id: int,
            db_session: AsyncSession
    ) -> dict:
        result = await db_session.scalars(select(User).where(User.id == user_id))
        user = result.one_or_none()

        if user is None:
            raise NotFoundException("User not found")

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
        data = data.dict()
        data["password"] = encrypt_password(data["password"])
        user = User(**data)
        db_session.add(user)
        await db_session.commit()
        return {
            "id": user.id,
            "name": user.name,
            "fullname": user.fullname,
        }

    @post("/login")
    async def login(
            self,
            data: dict,
            db_session: AsyncSession
    ) -> dict:
        return create_auth_token(data["email"], data["password"], db_session)

    @delete("/logout", status_code=200)
    async def logout(
            self,
            db_session: AsyncSession,
            token: str = Parameter(header="Authorization")
    ) -> dict:
        result = await db_session.scalars(select(AuthToken).where(AuthToken.token == token))
        auth_token = result.one_or_none()

        if auth_token is None:
            raise NotFoundException("Token not found")

        await db_session.delete(auth_token)
        await db_session.commit()
        return {
            "msg": "Logout successful"
        }
