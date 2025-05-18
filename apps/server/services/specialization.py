from sqlalchemy.orm import Session
from schemas.specialization import SpecializationBase
from app.db.models.specialization import Specialization
from typing import List


def get_all_specializations(db: Session) -> List[SpecializationBase]:
    items = db.query(Specialization).all()
    return [SpecializationBase.from_orm(item) for item in items]

