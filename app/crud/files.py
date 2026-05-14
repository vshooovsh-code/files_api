from collections import Counter

from app.models.files import FileStatistic, FileStatisticDetails


def get_file_statistic(name: str) -> FileStatistic | None:
    fs = read_file_get_statistic(name)
    return fs


def read_file_get_statistic(name: str) -> FileStatistic | None:
    fs = FileStatistic(name)
    try:
        with open(name, "r") as file:
            txt = ''
            for line in file:
                txt = txt + line
                fs.stat.rows_count =+1

            chars = dict(Counter(txt))
            fs.stat.stat = {'char_stat': chars, 'words_stat': 'None'}

        fs.read_success = True
        fs.message = 'Success'
        return fs

    except FileNotFoundError:
        fs.message = f"File {name} doesn’t exist"
        fs.read_success =False
    except Exception as ex:
        fs.message = str(ex)
        fs.read_success = False

    return fs