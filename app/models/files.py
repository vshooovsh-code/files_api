class FileStatisticDetails:
    chars_stat: dict

    def __init__(self):
        self.chars_stat = {}


class FileStatistic:
    name: str
    rows_count: int
    rows_total: bool
    stat: FileStatisticDetails

    def __init__(self, name: str) -> None:
        self.name: str = name
