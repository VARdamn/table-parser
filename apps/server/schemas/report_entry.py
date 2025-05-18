from pydantic import BaseModel
from datetime import datetime


class ReportEntryBase(BaseModel):
    report_id: int
    row_number: int
    group_id: int | None = None
    specialization_id: int | None = None
    subject_id: int | None = None


class ReportEntryCreate(ReportEntryBase):
    pass


class ReportEntryRead(ReportEntryBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
