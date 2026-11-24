from datetime import datetime, timedelta
from uuid import UUID

import jwt

from tin.auth.application.exceptions.invalid_access_token_error import InvalidAccessTokenError
from tin.auth.application.port.out.access_token_provider import AccessTokenProvider


class JwtAccessTokenProvider(AccessTokenProvider):

    def __init__(self,secret_key: str,algorithm: str,token_expire_minutes: int, token_type: str):
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.token_expire_minutes = token_expire_minutes
        self.token_type = token_type

    def generate_token(self, auth_id: UUID, now: datetime)-> str:

        payload:dict = {
            "sub": str(auth_id),
            "type": self.token_type,
            "iat": int(now.timestamp()),
            "exp": int((now + timedelta(minutes=self.token_expire_minutes)).timestamp())
        }

        return jwt.encode(payload=payload,key=self.secret_key, algorithm=self.algorithm)

    def verify_token(self, token: str) -> dict:
        try:
            claims = jwt.decode(
                jwt=token,
                key=self.secret_key,
                algorithms=[self.algorithm],
                options={"require": ["exp", "iat", "sub"]},
            )
        except jwt.ExpiredSignatureError as exc:
            raise InvalidAccessTokenError("access token has expired") from exc
        except jwt.InvalidTokenError as exc:
            raise InvalidAccessTokenError("invalid access token") from exc

        if claims.get("type") != self.token_type:
            raise InvalidAccessTokenError("not an access token")

        try:
            claims["sub"] = UUID(claims["sub"])
        except (ValueError, TypeError, AttributeError) as exc:
            raise InvalidAccessTokenError("invalid subject identifier") from exc
        return claims