from AFD import *

automatas2=Automatas()

class ER:

    def ExpresionesRegulares(self, er,tk):
            self.tokens2={
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
            "tk_asignacion": "=", 
            "tk_comentario_simple": automatas2.AFDComentarioSimple,
            "tk_division": "/",
            # "tk_comentario_var_filas": self.AFDComentarioVL,
            "tk_dato_double": automatas2.AFD_DatoTipoDouble,
            "tk_dato_tipo_Int": automatas2.AFD_DatoTipoInt,  
            "tk_dato_char": automatas2.AFD_DatoTipoChar,
            "tk_dato_string": automatas2.AFD_DatoTipoString,
            "tk_identificador": automatas2.AFD_Identificador,}

            self.expresionesregulares = {
            "tk_tipo_int":"int" ,
            "tk_tipo_double":"double",
            "tk_tipo_string":"string" ,
            "tk_tipo_char":"char",
            "tk_tipo_boolean":"boolean" ,
            "tk_suma":"+",
            "tk_resta": "-",
            "tk_multiplicacion":"*",
            "tk_resto":"%",
            "tk_diferenciacion":"!=" ,
            "tk_mayor_o_igual_que": ">=",
            "tk_mayor_que":">",
            "tk_menor_o_igual_que": "<=", 
            "tk_menor_que":"<" ,
            "tk_and": "&&",
            "tk_or": "||" ,
            "tk_not": "!",
            "tk_punto_coma": ";",
            "tk_condicional" :"if",
            "tk_par_abierto":"(" ,
            "tk_par_cerrado":  ")",
            "tk_llave_abierta":"{",
            "tk_llave_cerrada":"}",
            "tk_condicional_else":"else",
            "tk_iterativo_while":"while",
            "tk_iterativo_do":"do",
            "tk_reservda_void":"void" ,
            "tk_reservada_return": "return",
            "tk_igualacion": "==",
            "tk_asignacion":  "=", 
            "tk_comentario_simple": "//.*" ,
            "tk_division": "/" ,
            "tk_boolean_true":"true",
            "tk_boolean_false":"false",
            # "tk_comentario_var_filas": self.AFDComentarioVL,
            "tk_dato_double" : "dd+.dd*",
            "tk_dato_tipo_Int":"dd*", 
            "tk_dato_char":"\'.*\'",
            "tk_parametro":"\(.*,\)\*",
            "tk_dato_string":"\".*\"", 
            "tk_identificador":  "'_|L(_|L|d)*'",}
            match = dict()
            for token, patron in self.tokens2.items():
                if er == token:
                    match['patron'] = patron
                elif tk == token:
                    match['patron'] = patron
            for token, exp_reg in self.expresionesregulares.items():
                if er == token:
                    match['er'] = exp_reg
                elif tk == token:
                    match['er'] = exp_reg
            return match


