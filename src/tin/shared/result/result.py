from __future__ import annotations

from typing import Generic, TypeVar
from pydantic import BaseModel, model_validator

T = TypeVar("T")
E = TypeVar("E")

class Result(BaseModel, Generic[T,E]):
    success: bool
    data: T | None = None
    error: E | None = None

    @model_validator(mode="after")
    def validate_state(self):
        if self.success and (self.data is None or self.error is not None):
            raise ValueError("Success requires data and no error")
        if not self.success and (self.data is not None or self.error is None):
            raise ValueError("Failure requires an error and no data")
        return self

    @classmethod
    def ok(cls, data: T) -> Result[T,E]:
        return cls(
            success=True,
            data=data
        )

    @classmethod
    def fail(cls, error: E) -> Result[T,E]:
        return cls(
            success=False,
            error=error
        )