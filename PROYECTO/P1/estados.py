class Estados:
    def __init__(self, estado: str, caracter: str, lexema_reconocido: str, sig_estado: str ):
        self.estado = estado
        self.caracter = caracter
        self.lexema_reconocido = lexema_reconocido
        self.sig_estado = sig_estado


    def TE_ComentarioSimple(self,lexema_reconocido):
        pass

    def TE_ComentarioVariasLíneas(self,lexema_reconocido):
        pass

    def TE_DatoTipoInt(self,lexema_reconocido):
        # estados_def=['S0','S1']
        # estado=0
        # er="dd*"
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




        pass


    def TE_Identificador(self,lexema_reconocido):
        pass

    def TE_DatoTipoDouble(self,lexema_reconocido):
        pass


    def TE_DatoTipoString(self,lexema_reconocido):
        pass

    def TE_DatoTipoChar(self,lexema_reconocido):
        pass

