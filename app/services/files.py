from app.schemas.file import FileStatisticResponse


def get_file_statistic(name: str) -> FileStatisticResponse:
    result = FileStatisticResponse(name = name)
    return result