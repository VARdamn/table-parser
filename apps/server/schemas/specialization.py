from pydantic import BaseModel


class SpecializationBase(BaseModel):
	id: int
	
	name: str
	
	code: str | None = None

	model_config = {
		"from_attributes": True
	}
