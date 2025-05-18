from pydantic import BaseModel


class TeacherBase(BaseModel):
    full_name: str
    short_name: str | None = None
    employee_number: str | None = None


class TeacherCreate(TeacherBase):
    pass


class TeacherUpdate(TeacherBase):
    pass


class TeacherRead(TeacherBase):
    id: int

    class Config:
        orm_mode = True
