
from estados import *


class Rep_Estados:

    def reconocido_estados(self, tipo, lexema_reconocido):
        if tipo=='tk_dato_tipo_Int':
            tablaint=self.TE_DatoTipoInt(lexema_reconocido)
            c=Estados(tipo, lexema_reconocido,tablaint)
        elif tipo=='tk_dato_double':
            tabladouble=self.TE_DatoTipoDouble(lexema_reconocido)
            c=Estados(tipo, lexema_reconocido,tabladouble)
        elif tipo=='tk_identificador':
            tablaidentificador=self.TE_Identificador(lexema_reconocido)
            c=Estados(tipo, lexema_reconocido,tablaidentificador)
        elif tipo=='tk_comentario_simple':
            tablacomentariosimple=self.TE_ComentarioSimple(lexema_reconocido)
            c=Estados(tipo, lexema_reconocido,tablacomentariosimple)
        elif tipo=='tk_comentario_var_filas':
            tablacomentariosVL=self.TE_ComentarioVariasLíneas(lexema_reconocido)
            c=Estados(tipo, lexema_reconocido,tablacomentariosVL)
           
           
        return c

    def TE_ComentarioSimple(self,lexema_reconocido):
        estados_def = ['S0', 'S1', 'S2']
        i = 0
        size = 0
        reconocido = ''
        comentariosimple = list()
        while i < len(lexema_reconocido):
            if size == 0 and lexema_reconocido[i] == '/':
                caracter = lexema_reconocido[i]
                estado = estados_def[0]
                transicion = estados_def[1]
            elif size == 1 and lexema_reconocido[i] == '/':
                caracter = lexema_reconocido[i]
                estado = estados_def[1]
                transicion = estados_def[2]
            if size != 0 and transicion == 'S2':
                caracter = lexema_reconocido[i]
                estado = estados_def[2]
                transicion = estados_def[2]
            comentariosimple.append(
                [estado, caracter, reconocido, transicion])
            reconocido += lexema_reconocido[i]
            i += 1
            size += 1
        if i == len(lexema_reconocido):
            comentariosimple.append(
                [estado, '#', lexema_reconocido, transicion+'(aceptacion)'])
        return comentariosimple

    def TE_ComentarioVariasLíneas(self,lexema_reconocido):
        estados_def = ['S0', 'S1', 'S2','S3','S4']
        i = 0
        size = 0
        reconocido = ''
        ComentarioVL = list()
        while i < len(lexema_reconocido):
            if size == 0 and lexema_reconocido[i] == '/':
                caracter = lexema_reconocido[i]
                estado = estados_def[0]
                transicion = estados_def[1]
            elif size == 1 and lexema_reconocido[i] == '*':
                caracter = lexema_reconocido[i]
                estado = estados_def[1]
                transicion = estados_def[2]
            if size != 0 and transicion == 'S2' and i != (len(lexema_reconocido)-1):
                caracter = lexema_reconocido[i]
                estado = estados_def[2]
                transicion = estados_def[2]
            elif size != 0 and transicion == 'S2' and i == (len(lexema_reconocido)-1):
                caracter = lexema_reconocido[i]
                estado = estados_def[2]
                transicion = estados_def[3]
            ComentarioVL.append([estado, caracter, reconocido, transicion])
            reconocido += lexema_reconocido[i]
            i += 1
            size += 1

        if i == len(lexema_reconocido):
            ComentarioVL.append(
                [estados_def[3], '#', lexema_reconocido, estados_def[4] +'(aceptacion)'])
        return ComentarioVL

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
                estado=estados_def[0]
            else:
                estado=estados_def[1]
            caracter=lexema_reconocido[i]
            if i==0:
                transicion=estados_def[1]
            else:
                transicion=estados_def[1]
            entero.append([estado,caracter,reconocido,transicion])
            reconocido+=lexema_reconocido[i]
            i+=1
            size+=1
        if i==len(lexema_reconocido):
            entero.append([estado,"$",lexema_reconocido, transicion+'(aceptación)'])
        
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


    def TE_Identificador(self,lexema_reconocido):
        estados_def = ['S0','S1']
        i = 0
        size = 0
        reconocido = ''
        identificador = list()
        while i < len(lexema_reconocido):
            if size == 0 and not lexema_reconocido[i].isdigit():
                caracter = lexema_reconocido[i]
                estado = estados_def[0]
                transicion = estados_def[1]
            elif size != 0:
                caracter = lexema_reconocido[i]
                estado = estados_def[1]
                transicion = estados_def[1]
            identificador.append([estado, caracter, reconocido, transicion])
            reconocido += lexema_reconocido[i]
            i += 1
            size +=1
        if i == len(lexema_reconocido):
            identificador.append(
                [estado, '#', lexema_reconocido, transicion+'(aceptacion)'])
        return identificador

    def TE_DatoTipoDouble(self,lexema_reconocido):
        estados_def = ['S0', 'S1', 'S2', 'S3']
        i = 0
        size = 0
        er = 'd+.dd*'
        reconocido = ''
        double = list()
        while i < len(lexema_reconocido):
            if size == 0 and lexema_reconocido[i].isdigit():
                caracter = lexema_reconocido[i]
                estado = estados_def[0]
                transicion = estados_def[1]
            elif size == 0 and lexema_reconocido[i] == '.':
                caracter = lexema_reconocido[i]
                estado = estados_def[0]
                transicion = estados_def[2]
            if size != 0 and transicion == 'S1' and lexema_reconocido[i].isdigit():
                caracter = lexema_reconocido[i]
                estado = estados_def[1]
                transicion = estados_def[1]
            elif size != 0 and transicion == 'S1' and lexema_reconocido[i] == '.':
                caracter = lexema_reconocido[i]
                estado = estados_def[1]
                transicion = estados_def[2]
            elif size != 0 and transicion == 'S2' and lexema_reconocido[i].isdigit():
                caracter = lexema_reconocido[i]
                estado = estados_def[2]
                transicion = estados_def[3]
            if size != 0 and transicion == 'S2' and lexema_reconocido[i].isdigit():
                caracter = lexema_reconocido[i]
                estado = estados_def[2]
                transicion = estados_def[3]
            elif size != 0 and transicion == 'S3' and lexema_reconocido[i].isdigit():
                caracter = lexema_reconocido[i]
                estado = estados_def[2]
                transicion = estados_def[3]
            double.append(
                [estado, caracter, reconocido, transicion])
            reconocido += lexema_reconocido[i]
            i += 1
            size += 1
        if i == len(lexema_reconocido):
            double.append(
                [estado, '#', lexema_reconocido, transicion+'(aceptacion)'])
        return double


    def TE_DatoTipoString(self,lexema_reconocido):
        pass

    def TE_DatoTipoChar(self,lexema_reconocido):
        pass

