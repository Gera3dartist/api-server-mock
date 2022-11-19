import datetime
from uuid import uuid4
from pydantic import BaseModel, validator, Field

class DateTimeModelMixin(BaseModel):
    created_at: datetime.datetime = None
    updated_at: datetime.datetime = None

    @validator("created_at", "updated_at", pre=True, allow_reuse=True)
    def default_datetime(cls, value: datetime.datetime) -> datetime.datetime:
        return value or datetime.datetime.utcnow()


class IDModelMixin(BaseModel):
    id_: int = Field(alias="id")


class PublicIDModelMixin(BaseModel):
    public_id: str = Field(default_factory=lambda: str(uuid4()).replace('-', ''))
