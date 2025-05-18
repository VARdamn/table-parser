from fastapi import APIRouter, Depends
from app.db import get_db
from schemas.subject import SubjectBase
from services.subject import get_all_subjects
from typing import List
from sqlite3 import Connection

router = APIRouter(prefix="/subjects", tags=["subjects"])

@router.get("", response_model=List[SubjectBase])
def list_subjects(db: Connection = Depends(get_db)):
    return get_all_subjects(db)
