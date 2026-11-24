from abc import ABC, abstractmethod
from datetime import datetime
from uuid import UUID


class AccessTokenProvider(ABC):

    @abstractmethod
    def generate_token(self, auth_id: UUID, now: datetime) -> str:
        ...

    @abstractmethod
    def verify_token(self, token: str) -> dict:
        ...