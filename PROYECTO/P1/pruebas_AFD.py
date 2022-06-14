from os import startfile
import os

 
def AFDComentarioSimple(self,lexema):
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
        print(reconocido)

        if estado==-1:
            return False

    return estado in estados_aceptacion




print('\n','---------------------------------------------------', 'ANALIZADOR LÉXICO PARA SIMPLE C ','---------------------------------------------------')
print('MENÚ PRINCIPAL','\n')
contadorprocesos=0
while contadorprocesos>=0:
    question1=input('¿Desea iniciar el análisis léxico?'+'\n'+'Responda: si o no'+'\n')
    print('\n')
    if question1=='si': 
        #SELECCIÓN DE ARCHIVOS
        list_files= os.listdir('C:/Users/Linda Quelex/Desktop/UNIVERSIDAD 2022/(3.1) LAB LFP/PROYECTOS/PROYECTO1/LFP-VJ-201403745-P1/PROYECTO/ENTRADAS')
        print('\n')
        print('Archivos disponibles: ')
        for i in range(len(list_files)):
            print('Archivo ',i,':',list_files[i])
        print('\n')
        archivoseleccionado= input('Ingrese el nombre del archivo: ')
        print('El archivo a analizar es: ', archivoseleccionado) 
        #filename=list_files[int(archivoseleccionado)]   
        file = open( './ENTRADAS/'+ archivoseleccionado, encoding='utf-8')
        content = file.read()
        content2=content.lower()
        print('\n')
        print('Finalizó la carga de archivos','\n')
        # ENVIAR CONTENIDO AL ANALIZADOR LÉXICO
        AFDComentarioSimple(1,content2)