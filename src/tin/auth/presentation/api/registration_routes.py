from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from tin.auth.application.error.register_auth_error import RegisterAuthError
from tin.auth.application.port.inbound.register_with_password import RegisterWithPassword
from tin.auth.presentation.api.dto.register_with_password import (
    RegisterWithPasswordRequest,
    RegisterWithPasswordResponse,
)
from tin.auth.presentation.dependencies import get_register_with_password


router = APIRouter(prefix="/auth", tags=["auth-registration"])


@router.post(
    "/password",
    response_model=RegisterWithPasswordResponse,
    status_code=status.HTTP_201_CREATED,
    name="register_with_password",
)
async def register_with_password(
    request: RegisterWithPasswordRequest,
    use_case: Annotated[RegisterWithPassword, Depends(get_register_with_password)],
) -> RegisterWithPasswordResponse:
    result = await use_case.register_with_password(
        email=request.email,
        raw_password=request.password,
    )

    if not result.success:
        if result.error is RegisterAuthError.INVALID_EMAIL:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail={
                    "code": RegisterAuthError.INVALID_EMAIL.value,
                    "message": "The email address is invalid.",
                },
            )
        if result.error is RegisterAuthError.EMAIL_ALREADY_REGISTERED:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail={
                    "code": RegisterAuthError.EMAIL_ALREADY_REGISTERED.value,
                    "message": "An account with this email address already exists.",
                },
            )
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if result.data is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return RegisterWithPasswordResponse.model_validate(result.data)
