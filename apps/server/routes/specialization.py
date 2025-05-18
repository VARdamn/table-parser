from fastapi import APIRouter, Depends
from app.db import get_db
from schemas.specialization import SpecializationBase
from services.specialization import get_all_specializations
from typing import List
from sqlite3 import Connection

router = APIRouter(prefix="/specializations", tags=["specializations"])

@router.get("", response_model=List[SpecializationBase])
def list_specializations(db: Connection = Depends(get_db)):
    return get_all_specializations(db)
