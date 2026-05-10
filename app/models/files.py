class FileStatistic():
    name: str
    rows_count: int
    rows_total: bool

    def __init__(self, name: str) -> None:
        self.name: str = name
