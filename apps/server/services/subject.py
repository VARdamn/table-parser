from sqlalchemy.orm import Session
from schemas.subject import SubjectBase
from app.db.models.subject import Subject
from typing import List


def get_all_subjects(db: Session) -> List[SubjectBase]:
    items = db.query(Subject).all()
    return [SubjectBase.from_orm(item) for item in items]

