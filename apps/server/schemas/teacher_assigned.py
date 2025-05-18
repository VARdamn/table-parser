from pydantic import BaseModel


class TeacherAssignedBase(BaseModel):
    type: str
    teacher_id: int
    group_id: int
    subject_id: int


class TeacherAssignedCreate(TeacherAssignedBase):
    pass


class TeacherAssignedRead(TeacherAssignedBase):
    id: int

    class Config:
        orm_mode = True
