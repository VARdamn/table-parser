from sqlalchemy import Column, Integer, String
from app.db.session import Base

class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True)

    full_name = Column(String, nullable=False)

    short_name = Column(String)

    employee_number = Column(String, unique=True)
