from fastapi import FastAPI

from tin.auth.presentation.api.registration_routes import (
    router as password_registration_router,
)

app = FastAPI(title="Tin API")
app.include_router(password_registration_router)
