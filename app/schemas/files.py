from typing import ClassVar

from pydantic import BaseModel, ConfigDict


class FileStatisticDetailsResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    chars_stat: dict


class FileStatisticResponse(BaseModel):
    model_config = {'from_attributes': True}

    name: str
    rows_count: int
    read_success: bool
    stat: FileStatisticDetailsResponse
