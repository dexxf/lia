from datetime import datetime, timezone

from tin.auth.application.exceptions.invalid_email_error import InvalidEmailError
from tin.auth.application.error.register_auth_error import RegisterAuthError
from tin.auth.application.port.inbound.register_with_password import RegisterWithPassword
from tin.auth.application.port.outbound.auth_repository import AuthRepository
from tin.auth.application.port.outbound.email_validator import EmailValidator
from tin.auth.application.port.outbound.password_hasher import PasswordHasher
from tin.auth.application.result.register_auth_result import RegisterWithPasswordResult
from tin.shared.result.result import Result
from tin.auth.domain.entity.auth import Auth


class AuthRegistration(RegisterWithPassword):

    def __init__(self,password_hasher: PasswordHasher,auth_repository: AuthRepository,email_validator: EmailValidator,) -> None:
        self.password_hasher = password_hasher
        self.auth_repository = auth_repository
        self.email_validator = email_validator

    async def register_with_password(self,email: str,raw_password: str) -> Result[RegisterWithPasswordResult, RegisterAuthError]:
        try:
            normalized_email = self.email_validator.validate_and_normalize(email)
        except InvalidEmailError:
            return Result[RegisterWithPasswordResult, RegisterAuthError].fail(
                RegisterAuthError.INVALID_EMAIL
            )

        if await self.auth_repository.exists_by_email(normalized_email):
            return Result[RegisterWithPasswordResult, RegisterAuthError].fail(
                RegisterAuthError.EMAIL_ALREADY_REGISTERED
            )

        password_hash = self.password_hasher.hash(raw_password)

        now = datetime.now(timezone.utc)
        auth = Auth.create_new(
            email=normalized_email,
            now=now,
            password_hash=password_hash,
        )
        await self.auth_repository.save(auth)

        return Result[RegisterWithPasswordResult, RegisterAuthError].ok(
            RegisterWithPasswordResult(
                auth_id=str(auth.id),
                email=auth.email,
                created_at=auth.created_at,
            )
        )
