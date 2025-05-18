from fastapi import APIRouter, Depends
from app.db import get_db
from schemas.group import GroupBase
from services.group import get_all_groups
from typing import List
from sqlite3 import Connection

router = APIRouter(prefix="/groups", tags=["groups"])

@router.get("", response_model=List[GroupBase])
def list_groups(db: Connection = Depends(get_db)):
    return get_all_groups(db)
