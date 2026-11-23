from pwdlib import PasswordHash

from tin.auth.infrastructure.adapter.pwdlib_password_hasher import PwdlibPasswordHasher


class AuthContainer:

    def __init__(self):

        password_hasher = PasswordHash.recommended()
        self.pwd_lib_password_hasher = PwdlibPasswordHasher(password_hasher)




container = AuthContainer()