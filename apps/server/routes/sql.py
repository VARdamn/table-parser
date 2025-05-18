from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from schemas.sql import SQLRequest
from app.db import get_db

router = APIRouter(prefix="/sql", tags=["sql"])

@router.post("/execute")
def execute_sql(request: SQLRequest, db: Session = Depends(get_db)):
    try:
        result = db.execute(text(request.query))

        try:
            rows = result.mappings().all()
            return {"rows": [dict(row) for row in rows]}
        except Exception:
            db.commit()
            return {"message": "Query executed successfully, no result set"}
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail=f"SQL error: {str(e.orig) if hasattr(e, 'orig') else str(e)}"
        )
