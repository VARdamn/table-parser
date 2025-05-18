from fastapi import APIRouter, Depends
from app.db import get_db
from schemas.teacher import TeacherBase
from services.teacher import get_all_teachers
from typing import List
from sqlite3 import Connection

router = APIRouter(prefix="/teachers", tags=["teachers"])

@router.get("", response_model=List[TeacherBase])
def list_teachers(db: Connection = Depends(get_db)):
    return get_all_teachers(db)
