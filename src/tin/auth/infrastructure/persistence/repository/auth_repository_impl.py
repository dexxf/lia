from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from tin.auth.application.port.outbound.auth_repository import AuthRepository
from tin.auth.domain.entity.auth import Auth
from tin.auth.infrastructure.persistence.entity.auth_entity import AuthEntity
from tin.auth.infrastructure.persistence.mapper.auth_mapper import AuthMapper


class AuthRepositoryImpl(AuthRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def exists_by_email(self, email: str) -> bool:
        result = await self.session.execute(
            select(AuthEntity.id).where(AuthEntity.email == email)
        )
        return result.scalar_one_or_none() is not None

    async def save(self, auth: Auth) -> None:
        entity = AuthMapper.to_entity(auth)
        self.session.add(entity)
        await self.session.flush()

