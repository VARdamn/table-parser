from sqlalchemy import Column, Integer, String
from app.db.session import Base

class Specialization(Base):
    __tablename__ = "specializations"

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False, unique=True)

    code = Column(String, unique=True)
