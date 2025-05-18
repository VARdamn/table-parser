from sqlalchemy.orm import Session
from schemas.teacher import TeacherBase
from app.db.models.teacher import Teacher
from typing import List


def get_all_teachers(db: Session) -> List[TeacherBase]:
    items = db.query(Teacher).all()
    return [TeacherBase.from_orm(item) for item in items]

