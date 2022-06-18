
from errors import Errors
from token1 import Token1
from Rep_estados import *
from AFD import *
from ExR import *

automatas2= Automatas()
exp_R= ER()
r_estados=Rep_Estados()

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
        self.letra = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","á","é","í","ó","ú"]
        self.salto= '\n'

        self.tokens = {
        "tk_comentario_var_filas": automatas2.AFDComentarioVL,
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
                        continue

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
                    while siguiente <= len(entrada):# and entrada[siguiente - 1]:
                        lexema = entrada[posicion : siguiente]
                        estado_encontrado = patron(lexema)
                        aceptacion=estado_encontrado
                        #print(aceptacion)
                        #print(estado_encontrado)

                        # ! Error 
                        # if estado_encontrado!=False:
                            
                        #     self.list_estados.append(estado_encontrado[1])
                        #     print('hola',self.list_estados)

                        if not estado_encontrado and anterior:
                            lexema = entrada[posicion : siguiente - 1]
                            estado_encontrado = True
                            posicion = siguiente - 1
                            break
                        anterior = estado_encontrado
                        siguiente += 1

                    if estado_encontrado:
                        if '\n' in lexema:
                        #expresion=self.ExpresionesRegulares(token,patron)
                            expresion2=exp_R.ExpresionesRegulares(token)
                            # print(expresion["er"])
                            datos_token = Token1(fila,columna, lexema, token, expresion2['er'])
                            #enviar a método de estados
                            self.list_tokens.append(datos_token)
                            # print('llega1')
                            # estados=Estados("estado","caracter","lexema","siguiente estado")                   
                            # estados3=patron(lexema) 
                            # print('este es el estado 3', estados3[1])                
                            # self.list_estados.append(estados3[1])
                            enviar_estados=r_estados.reconocido_estados(token,lexema)
                            self.list_estados.append(enviar_estados)
                            # enviar_estados=r_estados.reconocido_estados(token,lexema)
                            # self.list_estados.append(enviar_estados)
                            #columna += siguiente - posicion + 1
                            posicion = siguiente - 1
                        else:
                            columna+=len(lexema)
                            expresion2=exp_R.ExpresionesRegulares(token)
                            # print(expresion["er"])
                            datos_token = Token1(fila,columna, lexema, token, expresion2['er'])
                            #enviar a método de estados
                       
                            self.list_tokens.append(datos_token)
                            # print('llega3')
                            # estados=Estados("estado","caracter","lexema","siguiente estado")                   
                            # estados3=patron(lexema) 
                            # print('este es el estado 3', estados3[1])                
                            # self.list_estados.append(estados3[1])
                            #columna += siguiente - posicion + 1

                            enviar_estados=r_estados.reconocido_estados(token,lexema)
                            self.list_estados.append(enviar_estados)
                    

                            posicion = siguiente - 1

                            # def arbol(self, tipo,lexema) -> list:
                                # constructor = ''
                                # if tipo == 'tk_dato_int':
                                #     valor_estado = self.EstadosNumeroEntero(lexema)
                                #     constructor = Buil(tipo,lexema,valor_estado)

                if estado_encontrado: break

            if not estado_encontrado:
                if siguiente>len(entrada):
                    lexema=entrada[posicion]
                
                datos_error = Errors(fila,columna, lexema)
                self.list_errors.append(datos_error)
                posicion += 1
               # print(datos_error.row, datos_error.col, datos_error.lexema)
        dt = {
        'tokens':self.list_tokens,
        'errores':self.list_errors,
        'estados':self.list_estados
        }
        return dt