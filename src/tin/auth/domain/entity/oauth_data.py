from __future__ import annotations

from dataclasses import dataclass
from typing import final
from uuid import UUID, uuid4

from tin.auth.domain.value_objects.oauth_provider import OAuthProvider

@final
@dataclass
class OAuthData:
    id: UUID
    oauth_provider: OAuthProvider
    provider_id: str

    def __post_init__(self) -> None:
        if self.id is None:
            raise ValueError("id must not be null")
        if self.oauth_provider is None:
            raise ValueError("oauth_provider must not be null")
        if self.provider_id is None:
            raise ValueError("provider_id must not be null")

    @classmethod
    def create_new(cls, oauth_provider: OAuthProvider, provider_id: str) -> OAuthData:
        return cls(id=uuid4(), oauth_provider=oauth_provider, provider_id=provider_id)

    @classmethod
    def reconstitute(cls, oauth_id: UUID, oauth_provider: OAuthProvider, provider_id: str) -> OAuthData:
        return cls(id=oauth_id, oauth_provider=oauth_provider, provider_id=provider_id)
