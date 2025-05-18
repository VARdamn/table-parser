from pydantic import BaseModel


class SpecializationBase(BaseModel):
    name: str
    code: str | None = None


class SpecializationCreate(SpecializationBase):
    pass


class SpecializationUpdate(SpecializationBase):
    pass


class SpecializationRead(SpecializationBase):
    id: int

    class Config:
        orm_mode = True
