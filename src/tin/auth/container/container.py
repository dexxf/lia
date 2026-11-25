from pwdlib import PasswordHash

from tin.auth.infrastructure.adapter.email_validator_impl import EmailValidatorAdapter
from tin.auth.infrastructure.adapter.pwdlib_password_hasher import PwdlibPasswordHasher
from tin.auth.infrastructure.adapter.jwt_access_token_provider import JwtAccessTokenProvider
from tin.shared.config.config import settings


class AuthContainer:

    def __init__(self):

        password_hasher = PasswordHash.recommended()
        self.pwd_lib_password_hasher = PwdlibPasswordHasher(password_hasher)

        self.email_validator = EmailValidatorAdapter()

        self.access_token_provider = JwtAccessTokenProvider(
            settings.JWT_SECRET_KEY,
            settings.JWT_ALGORITHM,
            settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES,
            "access")



container = AuthContainer()