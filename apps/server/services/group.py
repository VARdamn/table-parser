from sqlalchemy.orm import Session
from schemas.group import GroupBase
from app.db.models.group import Group
from typing import List


def get_all_groups(db: Session) -> List[GroupBase]:
    items = db.query(Group).all()
    print(items)
    return [GroupBase.from_orm(item) for item in items]

