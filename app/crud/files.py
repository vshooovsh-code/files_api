from app.models.files import FileStatistic, FileStatisticDetails


def get_file_statistic(name: str) -> FileStatistic | None:
    fs = read_file_get_statistic(name)
    return fs


def read_file_get_statistic(name: str) -> FileStatistic | None:
    fs = FileStatistic(name)
    try:
        with open(name, "r") as file:
            for line in file:
                # line.strip() удаляет лишние пробелы и символы переноса строки \n
                line = line.strip()

        fs.read_success = True
        return fs

    except FileNotFoundError:
        fs.message = f"File {name} doesn’t exist"
        fs.read_success =False
    except Exception as ex:
        fs.message = str(ex)
        fs.read_success = False

    return fs