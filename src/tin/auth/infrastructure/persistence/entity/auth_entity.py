from __future__ import annotations

from uuid import UUID
from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from tin.shared.persistence.base import Base

if TYPE_CHECKING:
    from tin.auth.infrastructure.persistence.entity.oauth_data_entity import OAuthDataEntity

class AuthEntity(Base):
    __tablename__ = "auth"

    id: Mapped[UUID] = mapped_column(
        "auth_id",
        primary_key=True,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
    )

    password_hash: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    oauth_data: Mapped[list[OAuthDataEntity]] = relationship(
        back_populates="auth",
        cascade="all, delete-orphan",
    )