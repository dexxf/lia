from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import final
from uuid import UUID, uuid4
from tin.auth.domain.entity.oauth_data import OAuthData


@final
@dataclass
class Auth:
    id: UUID
    email: str
    created_at: datetime
    updated_at: datetime
    password_hash: str | None = None
    _oauth_datas: list[OAuthData] = field(default_factory=list, repr=False)

    def __post_init__(self) -> None:
        if self.id is None:
            raise ValueError("id must not be null")
        if self.email is None:
            raise ValueError("email must not be null")
        if self.created_at is None:
            raise ValueError("created_at must not be null")
        if self.updated_at is None:
            raise ValueError("updated_at must not be null")
        if self._oauth_datas is None:
            raise ValueError("oauth_datas must not be null")
        self._oauth_datas = list(self._oauth_datas)

    @classmethod
    def create_new(cls, email: str, now: datetime, password_hash: str | None = None) -> Auth:
        return cls(
            id=uuid4(),
            email=email,
            created_at=now,
            updated_at=now,
            password_hash=password_hash
        )

    @classmethod
    def reconstitute(
        cls,
        auth_id: UUID,
        email: str,
        oauth_datas: list[OAuthData],
        created_at: datetime,
        updated_at: datetime,
        password_hash: str | None = None,
    ) -> Auth:
        if oauth_datas is None:
            raise ValueError("oauth_datas must not be null")
        return cls(
            id=auth_id,
            email=email,
            created_at=created_at,
            updated_at=updated_at,
            password_hash=password_hash,
            _oauth_datas=list(oauth_datas),
        )

    @property
    def oauth_datas(self) -> list[OAuthData]:
        return list(self._oauth_datas)

    def update_email(self, new_email: str, now: datetime) -> None:
        if new_email is None:
            raise ValueError("new_email must not be null")
        if now is None:
            raise ValueError("now must not be null")
        self.email = new_email
        self.updated_at = now

    def link_oauth_provider(self, oauth_data: OAuthData, now: datetime) -> bool:
        if oauth_data is None:
            raise ValueError("oauth_data must not be null")

        already_linked = any(data.oauth_provider == oauth_data.oauth_provider for data in self._oauth_datas)
        if already_linked:
            return False

        self._oauth_datas.append(oauth_data)
        self.updated_at = now
        return True

    def set_password_hash(self, password_hash: str, now: datetime) -> None:
        if password_hash is None:
            raise ValueError("password_hash must not be null")

        self.password_hash = password_hash
        self.updated_at = now
