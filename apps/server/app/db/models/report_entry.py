from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP, func, UniqueConstraint
from app.db.session import Base

class ReportEntry(Base):
    __tablename__ = "report_entries"
    __table_args__ = (UniqueConstraint("report_id", "row_number"),)

    id = Column(Integer, primary_key=True)

    report_id = Column(Integer, ForeignKey("reports.id", ondelete="CASCADE"), nullable=False)

    row_number = Column(Integer, nullable=False)

    group_id = Column(Integer, ForeignKey("groups.id"))

    specialization_id = Column(Integer, ForeignKey("specializations.id"))

    subject_id = Column(Integer, ForeignKey("subjects.id"))

    created_at = Column(TIMESTAMP, server_default=func.now())
