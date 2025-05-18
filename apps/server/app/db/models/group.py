from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, func
from app.db.session import Base

class Group(Base):
	__tablename__ = "groups"

	id = Column(Integer, primary_key=True)
  
	created_at = Column(TIMESTAMP, server_default=func.now())

	group_name = Column(String, nullable=False)
  
	group_code = Column(String, nullable=False, unique=True)
  
	specialization_id = Column(Integer, ForeignKey("specializations.id"))
  