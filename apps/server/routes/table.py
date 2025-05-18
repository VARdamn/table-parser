from fastapi import APIRouter

router = APIRouter(prefix="/table", tags=["table"])

@router.get("")
def load_teachers():
    return {"message": "table loaded"}
