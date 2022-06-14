
from errors import Errors
from token1 import Token1
from estados import Estados
from AFD import *
from ExR import *

automatas2= Automatas()
exp_R= ER()

class Lexico2:

    def __init__(self) -> None:
        self.list_tokens = list()
        self.list_errors = list()
        self.list_estados= list()
        self.list_estados=list()
        self.punto = ["."]
        self.g_bajo =['_']
        self.comillasimple=["'"]
        self.d = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.letra = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.salto= '\n'

        self.tokens = {
        "tk_parametro": automatas2.AFD_Parametro,
        "tk_tipo_int": "int",
        "tk_tipo_double": "double",
        "tk_tipo_string": "string",
        "tk_tipo_char": "char",
        "tk_tipo_boolean": "boolean",
        "tk_suma": "+",
        "tk_resta": "-",
        "tk_multiplicacion": "*",
        "tk_resto": "%",
        "tk_diferenciacion": "!=",
        "tk_mayor_o_igual_que": ">=",
        "tk_mayor_que": ">",
        "tk_menor_o_igual_que": "<=",
        "tk_menor_que": "<",
        "tk_and": "&&",
        "tk_or": "||",
        "tk_not": "!",
        "tk_punto_coma": ";",
        "tk_condicional": "if",
        "tk_par_abierto": "(",
        "tk_par_cerrado": ")",
        "tk_llave_abierta":"{",
        "tk_llave_cerrada":"}",
        "tk_condicional_else":"else",
        "tk_iterativo_while": "while",
        "tk_iterativo_do": "do",
        "tk_reservda_void": "void",
        "tk_reservada_return": "return",
        "tk_igualacion": "==",
        "tk_boolean_true":"true",
        "tk_boolean_false":"false",
        "tk_asignacion": "=",  #FALTA AGREGAR AL MANUAL TÉCNICO
        "tk_comentario_simple": automatas2.AFDComentarioSimple,
        "tk_division": "/",
        # "tk_comentario_var_filas": self.AFDComentarioVL,
        "tk_dato_double": automatas2.AFD_DatoTipoDouble,
        "tk_dato_tipo_Int": automatas2.AFD_DatoTipoInt,  #ESTA REPETIDO EL DATO INT EN EL MANUAL TÉCNICO
        "tk_dato_char": automatas2.AFD_DatoTipoChar,
        "tk_dato_string": automatas2.AFD_DatoTipoString,
        "tk_identificador": automatas2.AFD_Identificador,
        }
        self.i = " \n\t"

    def analizador(self,entrada):
        fila=1   
        columna=1
        posicion=0
        while posicion < len(entrada):
            caracter = entrada[posicion]
            estado_encontrado = False
            if caracter=="\n":     
                fila+=1                
                columna=1
            if caracter in self.i:
                posicion+=1
            for token, patron in self.tokens.items():
                if isinstance(patron, str):
                    if posicion + len(patron) > len(entrada): 
                        print('')
                    lexema = entrada[posicion : posicion + len(patron)]
                    if lexema == patron:
                        estado_encontrado = True
                        posicion += len(patron)
                        columna += len(patron)
                        datos_token = Token1(fila,columna, lexema, token, patron)
                        #print(datos_token.row, datos_token.col, datos_token.lexema, datos_token.token)
                        self.list_tokens.append(datos_token)
                else:
                    siguiente = posicion + 1
                    anterior = False
                    while siguiente <= len(entrada) and entrada[siguiente - 1] != self.salto :
                        lexema = entrada[posicion : siguiente]
                        estado_encontrado = patron(lexema)
                        if not estado_encontrado and anterior:
                            lexema = entrada[posicion : siguiente - 1]
                            estado_encontrado = True
                            posicion = siguiente - 1
                            break
                        anterior = estado_encontrado
                        siguiente += 1
                    if estado_encontrado:
                        #expresion=self.ExpresionesRegulares(token,patron)
                        expresion2=exp_R.ExpresionesRegulares(token,patron)
                        # print(expresion["er"])
                        datos_token = Token1(fila,columna, lexema, token, expresion2['er'])
                        self.list_tokens.append(datos_token)
                        #print(f"estado_encontrado: '{lexema}' | {token} - AFD")
                        columna += siguiente - posicion + 1
                        posicion = siguiente - 1
                if estado_encontrado: break
            if not estado_encontrado:
                posicion += 1
                datos_error = Errors(fila,columna, lexema)
                self.list_errors.append(datos_error)
                print(datos_error.row, datos_error.col, datos_error.lexema)
                print("ERROR LEXICO")
        dt = {'tokens':self.list_tokens,'errores':self.list_errors}
        return dt