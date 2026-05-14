class FileStatisticDetails:
    rows_count: int
    stat: dict

    def __init__(self):
        self.stat = {}
        self.rows_count = 0


class FileStatistic:
    name: str
    read_success: bool
    message: str
    stat: FileStatisticDetails

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.read_success = False
        self.message = ""
        self.stat = FileStatisticDetails()
