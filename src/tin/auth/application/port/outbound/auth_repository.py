from abc import ABC, abstractmethod

from tin.auth.domain.entity.auth import Auth


class AuthRepository(ABC):

    @abstractmethod
    async def exists_by_email(self, email: str) -> bool: ...

    @abstractmethod
    async def save(self, auth: Auth) -> None: ...
