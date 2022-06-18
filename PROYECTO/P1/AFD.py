from errors import Errors
from token1 import Token1
from estados import Estados


class Automatas:
    def __init__(self) -> None:
        self.punto = ["."]
        self.g_bajo =['_']
        self.comillasimple=["'"]
        self.d = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.l = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","á","é","í","ó","ú"]
        self.salto= '\n'
        self.comilladoble=['\"']

    def AFDComentarioSimple(self,lexema):  
        estado=0
        er="//.*"
        estados_aceptacion = [2]
        reconocido: str = ''        
        for caracter in lexema:
            if estado==0:
                if caracter =='/':
                    estado=1
                    reconocido+=caracter
                    # print(reconocido)
                else:
                    return False
            elif estado==1:
                if caracter =='/':
                    estado=2
                    reconocido+=caracter
                    # print(reconocido)
                else:
                    return False
            elif estado==2:
                if caracter.isalpha()and caracter !='\n':
                    reconocido+=caracter
                    estado=2       
                    # print(reconocido)
                elif not caracter.isalpha()and caracter !='\n':
                   reconocido+= caracter
                   estado=2
                elif caracter =='\n':
                    estado=3
                #    print(reconocido)
                else: 
                    return False

        #estados2=Estados(estado,caracter,reconocido,estado)
        # print(estados2.estado,estados2.caracter, estados2.lexema_reconocido, estados2.sig_estado)
        # self.list_estados.append(estados2)
        # print(reconocido)
        # print (estados2.lexema_reconocido)
        return estado in estados_aceptacion #estados2

    def AFDComentarioVL(self,lexema): # corregir
        estado=0
        er="\/\*.*\*\/"
        estados_aceptacion = [4]
        reconocido: str = ''        
        for caracter in lexema:
            if estado==0:
                if caracter =='/':
                    estado=1
                    reconocido+=caracter
                    # print(reconocido)
                else:
                    return False
            elif estado==1:
                if caracter =='*':
                    estado=2
                    reconocido+=caracter
                    # print(reconocido)
                else:
                    return False
            elif estado==2:
                if caracter != '*' and '/':
                    reconocido+=caracter
                    estado=2       
                    # print(reconocido)
                elif caracter =='*':
                    estado=3
                    
                elif caracter=='\n':
                    reconocido+=caracter
                    estado=3      
                    # print(reconocido)

                else: 
                    return False
            elif estado==3:
                if caracter =='*':
                    estado=3
                    reconocido+=caracter
                    # print(reconocido)
                elif caracter !='*' and caracter !='/':
                    estado=2
                    reconocido+=caracter
                elif caracter == '/':
                    estado=4
                    # print(reconocido)
                else: 
                    return False
            elif estado==4:
                return False
        # print(reconocido)
        return estado in estados_aceptacion 
    
    def AFD_DatoTipoInt(self,lexema):
        estado=0
        er="dd*"
        estados_aceptacion = [1]
        reconocido: str = ''
        for caracter in lexema:
            if estado==0:
                if caracter in self.d :
                    estado=1
                    reconocido+=caracter
                
                else:
                    return False
            elif estado==1:
                if caracter in self.d:
                    estado=1
                    reconocido+=caracter
                else:
                    return False
        #estados2=Estados(estado,caracter,reconocido,estado)
        return estado in estados_aceptacion #estados2

    def AFD_Identificador(self,lexema):
        estado=0 
        estados_aceptacion = [1]
        reconocido: str = ''
        er= '_|L(_|L|d)*'
        for caracter in lexema:
            if estado==0:
                if caracter in self.l :
                    estado=1
                    reconocido+=caracter
                elif caracter in self.g_bajo:
                    estado=1
                    reconocido+=caracter
                else:
                    return False
            elif estado==1:
                if caracter in self.l:
                    estado=1
                    reconocido+=caracter
                elif caracter in self.d:
                    estado=1
                    reconocido+=caracter
                elif caracter in self.g_bajo:
                    estado=1
                    reconocido+=caracter
                else:
                    return False
       #estados2=Estados(estado,caracter,reconocido,estado)
        return estado in estados_aceptacion #estados2

    def AFD_DatoTipoDouble(self,lexema): 
        estado=0
        er="d*.dd*"
        estados_aceptacion = [3]
        reconocido: str = ''
        for caracter in lexema:
            if estado==0:
                if caracter in self.d:
                    estado=1
                    reconocido+=caracter
                elif caracter =='.':
                    estado=2                  
                else:
                    return False
            elif estado==1:
                if caracter in self.d:
                    estado=1
                    reconocido+=caracter
                elif caracter =='.':
                    estado=2
                    reconocido+=caracter   #corregir porque acepta datos tipo int y tipo string
                else:
                    return False
            elif estado==2:
                if caracter in self.d:
                    estado= 3
                    reconocido+=caracter
                else:
                    return False
            elif estado==3:
                if caracter in self.d:
                    estado= 3
                    reconocido+=caracter
                else:
                    return False
         
        #print('impresión tipo double',reconocido)
        #estados2=Estados(estado,caracter,reconocido,estado)
       #print('estado',estado)
        return estado in estados_aceptacion #estados2

    def  AFD_DatoTipoString(self, lexema):
        estado=0 
        er= "\".*\""
        estados_aceptacion = [2]
        reconocido: str = ''
        for caracter in lexema:
            if estado==0:
                if caracter == '\"':
                    estado=1
                    reconocido+=caracter
                else:
                   estado=-1
            elif estado==1:
                if caracter != '"' and caracter !='\n':
                    estado=1
                    reconocido+=caracter
                elif caracter =='\n':
                    return False
                    reconocido+=caracter
                elif caracter =='"':
                    estado=2
                else: 
                    estado=-1
            elif estado==2: 
                estado=-1
            if estado==-1:
                estado=-1
        return estado in estados_aceptacion
    
    def AFD_DatoTipoChar(self,lexema):   #corregir
        estado=0 
        er= "\'.*\'"
        estados_aceptacion = [3]
        reconocido: str = ''
        for caracter in lexema:
            if estado==0:
                if caracter in self.comillasimple:
                    estado=1
                    reconocido+=caracter
                else:
                    return False
            elif estado==1:
                if caracter!='\n' and caracter not in self.comillasimple:
                    estado=2
                    reconocido+=caracter
                # elif caracter in self.comillasimple:
                #     estado=2
                else: 
                    return False
            elif estado==2: 
                if caracter in self.comillasimple:
                    estado=3
                    reconocido+=caracter
                else:
                    return False
            elif estado==3:
                return False
            
        #estados2=Estados(estado,caracter,reconocido,estado)
        return estado in estados_aceptacion #estados2