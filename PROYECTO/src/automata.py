import re
from utils.errors import Errors
from utils.token import Token
from typing import List



d=["0","1","2","3","4","5","6","7","8","9"]
L=["Ñ","ñ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


def AFDComentarioSimple(lexema):
    pass

def AFDComentarioVL(lexema):
    pass

def AFD_DatoTipoInt(lexema):
    pass

def AFD_Identificador(lexema):
    pass

def AFD_DatoTipoDouble(lexema):
    pass 

def  AFD_DatoTipoString(lexema):
    pass


def AFD_DatoTipoChar(lexema):
    pass

def AFD_DatoTipoBoolean(lexema):
    pass 

def AFD_Parametro(lexema):
    pass

# TOKENS DEFINIDOS
tokens = {
  "tk_comentario_simple": AFDComentarioSimple,
  "tk_comentario_var_lineas": AFDComentarioVL,
  "tk_tipo_int": "int",
  "tk_tipo_double": "double",
  "tk_tipo_string": "string",
  "tk_tipo_char": "char",
  "tk_tipo_boolean": "boolean",
  "tk_suma": "+",
  "tk_resta": "-",
  "tk_multiplicacion": "*",
  "tk_division": "/",
  "tk_resto": "%",
  "tk_asignacion": "=",  #falta agregar al manual técnico
  "tk_igualacion": "==",
  "tk_diferenciacion": "!=",
  "tk_mayor_que": ">",
  "tk_mayor_o_igual_que": ">=",
  "tk_menor_que": "<",
  "tk_menor_o_igual_que": "<=",
  "tk_and": "&&",
  "tk_or": "||",
  "tk_not": "!",
  "tk_punto_coma": ";",
  "tk_condicional": "if",
  "tk_par_abierto": "(",
  "tk_par_cerrado": ")",
  "tk_dato_tipo_Int": AFD_DatoTipoInt,  #ESTA REPETIDO EL DATO INT EN EL MANUAL TÉCNICO
  "tk_identificador": AFD_Identificador, 
  "tk_llave_abierta":"{",
  "tk_llave_cerrada":"}",
  "tk_condicional_else":"else",
  "tk_iterativo_while": "while",
  "tk_iterativo_do": "do",
  "tk_reservda_void": "void",
  "tk_reservada_return": "return",
  "tk_dato_double": AFD_DatoTipoDouble,
  "tk_dato_string": AFD_DatoTipoString,
  "tk_dato_char": AFD_DatoTipoChar,
  "tk_dato_boolean": AFD_DatoTipoBoolean,
  "tk_parametro": AFD_Parametro,
}

IGNORAR = " \n\t"




#FALTA REVISAR PARA UTILIZAR ESTE CÓDIGO O LA REPO, HAY QUE CONSIDERAR LOS REPORTES
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