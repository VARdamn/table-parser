from pydantic import BaseModel

class SQLRequest(BaseModel):
    query: str
