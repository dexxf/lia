from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from tin.auth.infrastructure.persistence.entity.oauth_data_entity import OAuthDataEntity
from tin.shared.persistence.base import Base


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

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    oauth_data: Mapped[list[OAuthDataEntity]] = relationship(
        back_populates="auth",
        cascade="all, delete-orphan",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )