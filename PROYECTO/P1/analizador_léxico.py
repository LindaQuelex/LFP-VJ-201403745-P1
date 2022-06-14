from turtle import pos
from errors import Errors
from token1 import Token1
from estados import Estados

class Lexico:

    def __init__(self) -> None:
        self.list_tokens = list()
        self.list_errors = list()
        self.list_estados= list()
        
        self.punto = ["."]
        self.g_bajo =['_']
        self.comillasimple=["'"]
        self.d = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.letra = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]



        self.tokens = {
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
        "tk_comentario_simple": self.AFDComentarioSimple,
        "tk_division": "/",
        # "tk_comentario_var_filas": self.AFDComentarioVL,
        "tk_dato_double": self.AFD_DatoTipoDouble,
        "tk_dato_tipo_Int": self.AFD_DatoTipoInt,  #ESTA REPETIDO EL DATO INT EN EL MANUAL TÉCNICO
        "tk_dato_char": self.AFD_DatoTipoChar,
        # "tk_parametro": self.AFD_Parametro,
        "tk_dato_string": self.AFD_DatoTipoString,

        "tk_identificador": self.AFD_Identificador,
        }

        self.expresionesregulares = {
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
        "tk_asignacion": "=",  #FALTA AGREGAR AL MANUAL TÉCNICO
        "tk_comentario_simple": "//.*",
        "tk_division": "/",
        "true":"tk_boolean_true",
        "false":"tk_boolean_false",
        # "tk_comentario_var_filas": self.AFDComentarioVL,
        "tk_dato_double": "dd+.dd*",
        "tk_dato_tipo_Int": "dd*",  #ESTA REPETIDO EL DATO INT EN EL MANUAL TÉCNICO
        # "tk_dato_char": self.AFD_DatoTipoChar,

        # "tk_parametro": self.AFD_Parametro,
        "tk_dato_string": "\".*\"",   #un string puede contener simbolos ???

         "'_|L(_|L|d)*'":"tk_identificador",
        }

        self.IGNORAR = " \n\t"

    def AFDComentarioSimple(self,lexema):  #no funciona en el analizador
        estado=0
        estados_aceptacion = [1]
        reconocido: str = ''
        for caracter in lexema:
            if estado==0:
                if caracter =='/':
                    estado=1
                    reconocido+=caracter
                else:
                    estado=-1
            elif estado==1:
                if caracter =='/':
                    estado=2
                    reconocido+=caracter
                else:
                    estado=-1
            elif estado==2:
                if caracter.isalpha():
                    reconocido+=caracter
                    estado=2       
                elif not caracter.isalpha():
                   reconocido+= caracter
                   estado=2
                else: 
                    estado=-1
            elif estado==2:
                if caracter=='\n':
                    print('aceptado')
                else:
                    estado=-1
            print(reconocido)
            if estado==-1:
                return False
        return estado in estados_aceptacion


    def AFDComentarioVL(lexema):
        pass

    def AFD_DatoTipoInt(self,lexema):
        estado=0
        estados_aceptacion = [1]
        for caracter in lexema:
            if estado==0:
                if caracter in self.d:
                    estado=1
                else:
                    estado=-1
            elif estado==1:
                if caracter in self.d:
                    estado=1
                else:
                    estado=-1
            if estado==-1:
                return False
        return estado in estados_aceptacion

    def AFD_Identificador(self,lexema):
        estado=0 
        estados_aceptacion = [1]
        er= '_|L(_|L|d)*'
        for caracter in lexema:
            if estado==0:
                if caracter in self.letra :
                    estado=1
                elif caracter in self.g_bajo:
                    estado=1
                else:
                    estado=-1
            elif estado==1:
                if caracter in self.letra:
                    estado=1
                elif caracter in self.d:
                    estado=1
                elif caracter in self.g_bajo:
                    estado=1
                else:
                    estado=-1
            if estado==-1:
                return False
        
        return estado in estados_aceptacion, er


    def AFD_DatoTipoDouble(self,lexema): #no funciona en el analizador
        estado=0
        estados_aceptacion = [1]

        for caracter in lexema:
            if estado==0:
                if caracter in self.d:
                    estado=1
                else:
                    estado=-1
            elif estado==1:
                if caracter =='.':
                    estado=2
                elif caracter in self.d:
                    estado=1
                # elif caracter == '.':
                #     estado=2
                else:
                    estado=-1
            elif estado==2:
                if caracter in self.d:
                    estado=3
                else:
                    estado=-1
            elif estado==3: 
                if caracter in self.d:
                    estado=3
                else:
                    estado=-1

            if estado==-1:
                return False

        return estado in estados_aceptacion


    def  AFD_DatoTipoString(self, lexema):
        estado=0 
        estados_aceptacion = [1]
        for caracter in lexema:
            if estado==0:
                if caracter =='"':
                    estado=1
                else:
                    estado=-1
            elif estado==1:
                if caracter.isalpha():
                    estado=1
                elif not caracter.isalpha():
                    estado=1
                else: 
                    estado=2
            elif estado==2: 
                if caracter=='"':
                    estado=1
                else:
                    estado=-1
            if estado==-1:
                return False
        return estado in estados_aceptacion
    
    def AFD_DatoTipoChar(self,lexema):  #el tipo char solo trae un caracter?
        estado=0 
        estados_aceptacion = [1]
        for caracter in lexema:
            if estado==0:
                if caracter in self.comillasimple:
                    estado=1
                else:
                    estado=-1
            elif estado==1:
                if caracter.isalpha():
                    estado=1
                elif not caracter.isalpha():
                    estado=1
                else: 
                    estado=2
            elif estado==2: 
                if caracter in self.comillasimple:
                    estado=1
                else:
                    estado=-1
            if estado==-1:
                return False
        return estado in estados_aceptacion

    def AFD_Parametro(lexema):
        pass

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
        
            if caracter in self.IGNORAR:
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
                        
                else: # AFD
                
                    siguiente = posicion + 1
                    anterior_estado_encontrado = False

                    while siguiente <= len(entrada) and entrada[siguiente - 1] != '\n' :
                        lexema = entrada[posicion : siguiente]
                        estado_encontrado = patron(lexema)
                        

                        if not estado_encontrado and anterior_estado_encontrado :
                            lexema = entrada[posicion : siguiente - 1]
                            estado_encontrado = True
                            posicion = siguiente - 1
                            break

                        anterior_estado_encontrado = estado_encontrado
                        siguiente += 1

                    if estado_encontrado:
                        datos_token = Token1(fila,columna, lexema, token, lexema)
                        self.list_tokens.append(datos_token)
                        print(f"estado_encontrado: '{lexema}' | {token} - AFD")
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



