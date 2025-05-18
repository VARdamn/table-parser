from pydantic import BaseModel
from datetime import datetime


class GroupBase(BaseModel):

	id: int

	created_at: datetime

	group_name: str

	group_code: str

	specialization_id: int | None = None
	
	model_config = {
		"from_attributes": True
	}
