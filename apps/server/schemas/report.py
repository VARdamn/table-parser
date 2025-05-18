from pydantic import BaseModel
from datetime import datetime


class ReportBase(BaseModel):
	id: int

	created_at: datetime

	created_by: str | None = None

	filename: str | None = None

	file_hash: str

	model_config = {
		"from_attributes": True
	}
