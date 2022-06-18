
from estados import *


class Rep_Estados:

    def reconocido_estados(self, tipo, lexema_reconocido):
        if tipo=='tk_dato_tipo_Int':
            t=self.TE_DatoTipoInt(lexema_reconocido)
            c=Rep_Estados(tipo, lexema_reconocido,t)
        return c



    def TE_ComentarioSimple(self,lexema_reconocido):
        pass

    def TE_ComentarioVariasLíneas(self,lexema_reconocido):
        pass

    def TE_DatoTipoInt(self,lexema_reconocido):
     
        estados_def=['S0','S1']
        i=0
        size=0
        er="dd*"
        reconocido=''
        entero=list()
        contador=0
        while i < len(lexema_reconocido):
            if size==0:
                estado=f'{estados_def[0]}'
            else:
                estado=f'{estados_def[1]}'
            caracter=lexema_reconocido[i]
            if i==0:
                transicion=f'{estados_def[1]}'
            else:
                transicion=f'{estados_def[1]}'
            entero.append([estado,caracter,reconocido,transicion])
            reconocido+=lexema_reconocido[i]
            i+=1
            size+=1
        if i==len(lexema_reconocido):
            entero.append([estado,"$",lexema_reconocido, transicion])

        return entero
        # estados_aceptacion = [1]
        # reconocido: str = ''
        # for caracter in lexema:
        #     if estado==0:
        #         if caracter in self.d :
        #             estado=1
        #             reconocido+=caracter
                
        #         else:
        #             return False
        #     elif estado==1:
        #         if caracter in self.d:
        #             estado=1
        #             reconocido+=caracter
        #         else:
        #             return False


#ejemplo Santi
        # indice = 0
        # large = 0
        # lexema_reade = ''
        # estadoNumEntero = list()
        # while indice < len(lexema):
        #     if large == 0:
        #         estado = f'{lista_estados[0]}'
        #     else:
        #         estado = f'{lista_estados[1]}'
            
        #     caracter = lexema[indice]
            
        #     if indice == 0:
        #         transicion = f'{lista_estados[1]}'
        #     else:
        #         transicion = f'{lista_estados[1]}'
                
        #     estadoNumEntero.append([estado, caracter, lexema_reade, transicion])
        #     lexema_reade += lexema[indice]
        #     indice += 1
        #     large +=1
        
        # if indice == len(lexema):
        #     estadoNumEntero.append(
        #         [estado, '#', lexema, f'{transicion} -> (aceptacion)'])

        
        # return estadoNumEntero



    def TE_Identificador(self,lexema_reconocido):
        pass

    def TE_DatoTipoDouble(self,lexema_reconocido):
        pass


    def TE_DatoTipoString(self,lexema_reconocido):
        pass

    def TE_DatoTipoChar(self,lexema_reconocido):
        pass

