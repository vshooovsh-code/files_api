from app.models.files import FileStatistic, FileStatisticDetails


def get_file_statistic(name: str) -> FileStatistic | None:
    fs = FileStatistic(name)
    fs.rows_count = 5
    fs.read_success = True

    fsd = FileStatisticDetails()
    fsd.chars_stat ={'a': 10}
    fs.stat = fsd
    return fs
