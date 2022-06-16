from AFD import *

automatas2=Automatas()

class ER:

    def ExpresionesRegulares(self, tk):
           
            expresionesregulares = {
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
            "tk_menor_o_igual_que": "<=", 
            "tk_menor_que":"<" ,
            "tk_mayor_que":">",
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
            "tk_comentario_var_filas": "\/\*.*\*\/",
            "tk_dato_double" : "dd+.dd*",
            "tk_dato_tipo_Int":"dd*", 
            "tk_dato_char":"\'.*\'",
            "tk_dato_string":"\".*\"", 
            "tk_identificador":  "'_|L(_|L|d)*'",}
            match = dict()
            for token, exp_reg in expresionesregulares.items():
                if tk == token:
                    match['er'] = exp_reg
            return match


