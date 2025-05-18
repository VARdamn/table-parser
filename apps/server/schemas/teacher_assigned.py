from pydantic import BaseModel


class TeacherAssignedBase(BaseModel):

	id: int
	
	type: str

	teacher_id: int

	group_id: int

	subject_id: int

	model_config = {
		"from_attributes": True
	}
