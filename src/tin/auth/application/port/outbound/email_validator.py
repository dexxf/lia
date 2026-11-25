from typing import Protocol


class EmailValidator(Protocol):
    def validate_and_normalize(self,email:str) -> str: ...