from sqlalchemy import Column, Integer, ForeignKey
from app.db.session import Base

class GroupSubject(Base):
	__tablename__ = "group_subjects"

	group_id = Column(Integer, ForeignKey("groups.id", ondelete="CASCADE"), primary_key=True)
	
	subject_id = Column(Integer, ForeignKey("subjects.id", ondelete="CASCADE"), primary_key=True)
