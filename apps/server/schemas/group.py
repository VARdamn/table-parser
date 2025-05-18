from pydantic import BaseModel
from datetime import datetime


class GroupBase(BaseModel):
    group_name: str
    group_code: str
    specialization_id: int | None = None


class GroupCreate(GroupBase):
    pass


class GroupUpdate(GroupBase):
    pass


class GroupRead(GroupBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
