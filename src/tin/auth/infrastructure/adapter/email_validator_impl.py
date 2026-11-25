from email_validator import validate_email


class EmailValidatorAdapter:

    def validate_and_normalize(self, email: str) -> str:
        result = validate_email(
            email,
            check_deliverability=False,
            allow_smtputf8=True,
            allow_display_name=False,
        )

        return result.normalized