from pydantic import BaseModel
from datetime import datetime


class ReportEntryBase(BaseModel):

	id: int

	created_at: datetime

	report_id: int

	row_number: int

	group_id: int | None = None

	specialization_id: int | None = None

	subject_id: int | None = None
	
	model_config = {
		"from_attributes": True
	}
	