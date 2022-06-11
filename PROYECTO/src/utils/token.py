class Token:
    def __init__(self, row: int, col: int, lexema: str, token: str, patron:str ):
        self.lexema = lexema
        self.token = token
        self.row = row
        self.col = col
        self.patron= patron