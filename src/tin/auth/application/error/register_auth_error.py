from enum import Enum


class RegisterAuthError(str, Enum):
    INVALID_EMAIL = "invalid_email"
    EMAIL_ALREADY_REGISTERED = "email_already_registered"
