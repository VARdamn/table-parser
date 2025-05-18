from pydantic import BaseModel


class TeacherBase(BaseModel):
    
	id: int

	full_name: str
    
	short_name: str | None = None
    
	employee_number: str | None = None

	model_config = {
		"from_attributes": True
	}
    