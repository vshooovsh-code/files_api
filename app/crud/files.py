from app.models.files import FileStatistic


def get_file_statistic(name: str) -> FileStatistic|None:
    fs = FileStatistic(name)
    fs.rows_count =5
    fs.read_success = True
    return fs