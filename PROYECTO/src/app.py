from os import startfile
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape
from automata import automata



print('\n','---------------------------------------------------', 'ANALIZADOR LÉXICO PARA SIMPLE C ','---------------------------------------------------')
print('MENÚ PRINCIPAL','\n')
contadorprocesos=0
while contadorprocesos>=0:
    question1=input('¿Desea iniciar el análisis léxico?'+'\n'+'Responda: si o no'+'\n')
    print('\n')
    try:
        if question1=='si': 
            #SELECCIÓN DE ARCHIVOS
            list_files= os.listdir('C:/Users/Linda Quelex/Desktop/UNIVERSIDAD 2022/(3.1) LAB LFP/PROYECTOS/taller-lfp-main/ENTRADAS')
            print('\n')
            print('Archivos disponibles: ')
            for i in range(len(list_files)):
                print('Archivo ',i,':',list_files[i])
            print('\n')
            archivoseleccionado= input('Ingrese el nombre del archivo: ')
            print('El archivo a analizar es: ', archivoseleccionado) 
            #filename=list_files[int(archivoseleccionado)]   
            file = open( './ENTRADAS/'+ archivoseleccionado, encoding='utf-8')
            #CONVERTIR EL CONTENIDO A MINUSCULAS
            #INSERTAR MÉTODO ANALIZADOR LÉXICO
            content = file.read()
            print('\n')
            print('Finalizó la carga de archivos','\n')

            #INGRESAR EL NOMBRE DEL ARCHIVO DE SALIDA
    except: 
        print('\n','-------------------------------------')
        print('El archivo no existe intente de nuevo')
        print('\n','-------------------------------------')

    print('\n')
    salir=input('¿Desea intentar de nuevo?' +'\n'+'Responda: si o no'+'\n')
    if salir=='si':
        contadorprocesos+=1
    else: 
        salir=input('¿Desea salir de la aplicación?' +'\n'+'Responda: si o no'+'\n')
        if salir=='si':
            exit()
        else: 
            contadorprocesos+=1


















# funcionamiento del analizador léxico
    tokens, errs = automata(content)

    env = Environment(loader=FileSystemLoader('src/templates'),
                      autoescape=select_autoescape(['html']))

    template = env.get_template('symbol_table.html')
    html_file = open('output.html', 'w+', encoding='utf-8')
    html_file.write(template.render(tokens=tokens, errs=errs))
    html_file.close()

    startfile('output.html')
