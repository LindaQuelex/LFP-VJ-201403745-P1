import re
from utils.errors import Errors
from utils.token import Token
from typing import List


# Tokens

tokens = {
  "tk_reservada_inicio": "INICIO",
  "tk_reservada_fin": "FIN",
  "tk_operador_suma": "+",
  "tk_operador_resta": "-",
  "tk_operador_multiplicacion": "*",
  "tk_operador_division": "/",
  "tk_operador_resto": "%",
  "tk_operador_igualacion": "==",
  "tk_operador_asignacion": "=",
  "tk_operador_resto": "%",
#   "tk_numero_double": AFDNumeroDouble
#   "tk_numero": AFDNumero
}

IGNORAR = " \n\t"






digito=["0","1","2","3","4","5","6","7","8","9"]
letra=["a","b","c","d","e","f","g","h","i","j"]



def automata(input: str):
    # variables temporales
    lexema: str = ''
    state: int = 1
    i: int = 0
    row: int = 1
    col: int = 1

    # lista de tokens
    tokens: List[Token] = []

    # lista de errores
    errors: List[Errors] = []

    while i < len(input):
        char: str = input[i]

        if state == 1:
            if char == '=':
                state = 8
                i += 1
                lexema += char
                col += 1
            elif char == '"':
                state = 2
                i += 1
                lexema += char
                col += 1
            elif char.isalpha():
                state = 5
                i += 1
                lexema += char
                col += 1
            elif char.isdigit():
                state = 4
                i += 1
                lexema += char
                col += 1

            # Caracteres ignorados
            elif re.search(r'[\n]', char):
                row += 1
                col = 1
                i += 1
            elif re.search(r'[ ]', char):
                col += 1
                i += 1
            elif re.search(r'[\t]', char):
                col += 3
                i += 1

            # manejo de errores
            else:
                errors.append(Errors(char, row, col))
                i += 1
                col += 1
                state = 1
                lexema = ''

        elif state == 2:
            if char.isalnum() or char == ' ':
                i += 1
                lexema += char
                col += 1
            elif char == '"':
                state = 3
                i += 1
                lexema += char
                col += 1
            # manejo de errores
            else:
                errors.append(Errors(char, row, col))
                i += 1
                col += 1
                state = 1
                lexema = ''
        elif state == 3:
            tokens.append(Token('str', lexema, row, col))
            lexema = ''
            state = 1
        elif state == 4:
            if char.isdigit():
                i += 1
                lexema += char
                col += 1
            elif char == '.':
                state = 6
                i += 1
                lexema += char
                col += 1
            else:
                tokens.append(Token('int', lexema, row, col))
                lexema = ''
                state = 1
        elif state == 5:
            if char.isdigit() or char.isalpha() or char == '_':
                i += 1
                lexema += char
                col += 1
            else:
                tokens.append(Token('id', lexema, row, col))
                lexema = ''
                state = 1
        elif state == 6:
            if char.isdigit():
                state = 7
                i += 1
                lexema += char
                col += 1
            # manejo de errores
            else:
                errors.append(Errors(char, row, col))
                i += 1
                col += 1
                state = 1
                lexema = ''
        elif state == 7:
            if char.isdigit() or char.isalpha() or char == '_':
                i += 1
                lexema += char
                col += 1
            else:
                tokens.append(Token('double', lexema, row, col))
                lexema = ''
                state = 1
        elif state == 8:
            tokens.append(Token('equals', lexema, row, col))
            lexema = ''
            state = 1

    return tokens, errors