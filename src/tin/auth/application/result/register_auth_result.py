from datetime import datetime

from pydantic import BaseModel

class RegisterWithPasswordResult(BaseModel):
    auth_id: str
    email: str
    created_at: datetime
