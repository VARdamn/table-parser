from pydantic import BaseModel


class SubjectBase(BaseModel):
    name: str
    code: str | None = None


class SubjectCreate(SubjectBase):
    pass


class SubjectUpdate(SubjectBase):
    pass


class SubjectRead(SubjectBase):
    id: int

    class Config:
        orm_mode = True
