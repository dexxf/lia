from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from tin.auth.application.port.inbound.register_with_password import RegisterWithPassword
from tin.auth.application.service.register_auth import AuthRegistration
from tin.auth.container.container import container
from tin.auth.infrastructure.persistence.repository.auth_repository_impl import (
    AuthRepositoryImpl,
)
from tin.shared.persistence.session import get_session


def get_register_with_password(session: Annotated[AsyncSession, Depends(get_session, scope="function")]) -> RegisterWithPassword:
    return AuthRegistration(
        password_hasher=container.pwd_lib_password_hasher,
        auth_repository=AuthRepositoryImpl(session),
        email_validator=container.email_validator,
    )
