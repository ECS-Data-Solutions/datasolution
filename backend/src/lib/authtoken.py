from src.lib.encrypt import encrypt_password
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.AuthToken import AuthToken, CreateAuthTokenDTO
from src.models.User import User
from sqlalchemy import select
from starlite import NotFoundException
from random import randbytes


async def create_auth_token(email: str, password: str, db_session: AsyncSession) -> dict:
    # Check user email and Password
    user_result = await db_session.scalars(select(User).where(User.email == email))
    user = user_result.one_or_none()

    if user is None:
        raise NotFoundException("User not found")

    if user.password != encrypt_password(password):
        raise NotFoundException("Authentication failed")

    # Create Auth Token
    auth_dto = CreateAuthTokenDTO(user_id=user.id, token=randbytes(32).hex())
    auth_token = AuthToken(**auth_dto.dict())

    db_session.add(auth_token)
    await db_session.commit()

    return {
        "msg": "Authentication successful",
        "token": auth_token.token
    }



