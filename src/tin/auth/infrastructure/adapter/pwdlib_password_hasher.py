from pwdlib import PasswordHash

class PwdlibPasswordHasher:

    def __init__(self, password_hash: PasswordHash) -> None:
        self._password_hash: PasswordHash = password_hash

    def hash(self, password: str) -> str:
        return self._password_hash.hash(password)

    def verify(self, password: str, password_hash: str) -> bool:
        return self._password_hash.verify(password, password_hash)
