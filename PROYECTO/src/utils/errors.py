class Errors:
    def __init__(self,  row: int, col: int, lexema: str) -> None:
        self.lexema = lexema
        self.row = row
        self.col = col