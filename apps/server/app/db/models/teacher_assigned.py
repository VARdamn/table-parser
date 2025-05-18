from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from app.db.session import Base

class TeacherAssigned(Base):
    __tablename__ = "teacher_assigned"
    __table_args__ = (
        UniqueConstraint("type", "teacher_id", "group_id", "subject_id"),
    )

    id = Column(Integer, primary_key=True)

    type = Column(String)

    teacher_id = Column(Integer, ForeignKey("teachers.id", ondelete="CASCADE"), nullable=False)

    group_id = Column(Integer, ForeignKey("groups.id", ondelete="CASCADE"), nullable=False)

    subject_id = Column(Integer, ForeignKey("subjects.id", ondelete="CASCADE"), nullable=False)
