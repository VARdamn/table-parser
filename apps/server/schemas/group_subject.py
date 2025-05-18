from pydantic import BaseModel


class GroupSubjectBase(BaseModel):
	
	group_id: int

	subject_id: int

	model_config = {
		"from_attributes": True
	}
