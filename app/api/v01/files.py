
from fastapi import APIRouter, Depends, Query

from app.schemas.file import FileStatisticResponse
from app.services import files as service_files

router = APIRouter()
@router.get("/files/statistic", response_model=FileStatisticResponse)
def get_operations(
        name: str ):
    return service_files.get_file_statistic(name)
