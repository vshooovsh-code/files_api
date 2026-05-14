from typing import ClassVar

from pydantic import BaseModel, ConfigDict


class FileStatisticDetailsResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    rows_count: int
    stat: dict


class FileStatisticResponse(BaseModel):
    model_config = {'from_attributes': True}

    name: str
    read_success: bool
    message: str
    stat: FileStatisticDetailsResponse
