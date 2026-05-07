from pydantic import BaseModel, Field, field_validator

class FileStatisticResponse(BaseModel):
    model_config = {
        'from_attributes': True}
    name: str

