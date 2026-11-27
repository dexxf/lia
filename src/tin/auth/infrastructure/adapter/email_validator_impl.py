from email_validator import validate_email
from email_validator import EmailNotValidError

from tin.auth.application.exceptions.invalid_email_error import InvalidEmailError


class EmailValidatorAdapter:

    def validate_and_normalize(self, email: str) -> str:
        try:
            result = validate_email(
                email,
                check_deliverability=False,
                allow_smtputf8=True,
                allow_display_name=False,
            )
        except EmailNotValidError as exc:
            raise InvalidEmailError from exc

        return result.normalized