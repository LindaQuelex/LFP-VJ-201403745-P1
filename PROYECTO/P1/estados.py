class Estados:
    def __init__(self, estado: str, caracter: str, lexema_reconocido: str, sig_estado: str ):
        self.estado = estado
        self.caracter = caracter
        self.lexema_reconocido = lexema_reconocido
        self.sig_estado = sig_estado