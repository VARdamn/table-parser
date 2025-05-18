from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from app.db.session import Base

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True)

    created_at = Column(TIMESTAMP, server_default=func.now())

    created_by = Column(String(100))

    filename = Column(String)

    file_hash = Column(String(64), unique=True)
