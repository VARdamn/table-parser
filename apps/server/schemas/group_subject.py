from pydantic import BaseModel


class GroupSubjectBase(BaseModel):
    group_id: int
    subject_id: int


class GroupSubjectCreate(GroupSubjectBase):
    pass


class GroupSubjectRead(GroupSubjectBase):
    class Config:
        orm_mode = True
