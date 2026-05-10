from app.schemas.files import FileStatisticResponse
from app.crud import  files as crud_files


def get_file_statistic(name: str) -> FileStatisticResponse:
    fs =crud_files.get_file_statistic(name)
    if not fs:
        result = FileStatisticResponse(name=name, row_count=0, read_success=False)
        return result
    else:
        result = FileStatisticResponse.model_validate(fs)
        return result