from abc import ABC, abstractmethod

from tin.auth.application.error.register_auth_error import RegisterAuthError
from tin.auth.application.result.register_auth_result import RegisterWithPasswordResult
from tin.shared.result.result import Result


class RegisterWithPassword(ABC):
    @abstractmethod
    async def register_with_password(
        self,
        email: str,
        raw_password: str,
    ) -> Result[RegisterWithPasswordResult, RegisterAuthError]: ...
