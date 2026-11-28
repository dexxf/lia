from tin.auth.domain.entity.auth import Auth
from tin.auth.domain.entity.oauth_data import OAuthData
from tin.auth.domain.value_objects.oauth_provider import OAuthProvider
from tin.auth.infrastructure.persistence.entity.auth_entity import AuthEntity
from tin.auth.infrastructure.persistence.entity.oauth_data_entity import OAuthDataEntity

class AuthMapper:
    @staticmethod
    def to_entity(auth: Auth) -> AuthEntity:
        return AuthEntity(
            id=auth.id,
            email=auth.email,
            password_hash=auth.password_hash,
            created_at=auth.created_at,
            updated_at=auth.updated_at,
            oauth_data=[
                OAuthDataEntity(id=oauth_data.id,oauth_provider=oauth_data.oauth_provider.name,provider_id=oauth_data.provider_id)
                for oauth_data in auth.oauth_datas
            ],
        )

    @staticmethod
    def to_domain(auth_entity: AuthEntity) -> Auth:
        return Auth.reconstitute(
            auth_id=auth_entity.id,
            email=auth_entity.email,
            oauth_datas=[
                OAuthData.reconstitute(oauth_id=oauth_data.id,oauth_provider=OAuthProvider[oauth_data.oauth_provider],provider_id=oauth_data.provider_id)
                for oauth_data in auth_entity.oauth_data
            ],
            created_at=auth_entity.created_at,
            updated_at=auth_entity.updated_at,
            password_hash=auth_entity.password_hash,
        )
