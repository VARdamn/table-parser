from pydantic import BaseModel
from datetime import datetime


class ReportBase(BaseModel):
    created_by: str | None = None
    filename: str | None = None
    file_hash: str


class ReportCreate(ReportBase):
    pass


class ReportRead(ReportBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

