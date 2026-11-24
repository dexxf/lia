from uuid import UUID

from sqlalchemy import (
    ForeignKey,
    String,
    UniqueConstraint
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from tin.auth.infrastructure.persistence.entity.auth_entity import AuthEntity
from tin.shared.persistence.base import Base


class OAuthDataEntity(Base):
    __tablename__ = "oauth_data"

    __table_args__ = (
        UniqueConstraint(
            "oauth_provider",
            "provider_id",
            name="uk_oauth_provider",
        ),
    )

    id: Mapped[UUID] = mapped_column(
        "oauth_data_id",
        primary_key=True,
    )

    auth_id: Mapped[UUID] = mapped_column(
        ForeignKey("auth.auth_id"),
        nullable=False,
    )

    auth: Mapped[AuthEntity] = relationship(
        back_populates="oauth_data",
    )

    oauth_provider: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    provider_id: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )