from pydantic import BaseModel

class FileStatisticResponse(BaseModel):
    model_config = {'from_attributes': True}

    name: str
    rows_count: int
    read_success: bool
