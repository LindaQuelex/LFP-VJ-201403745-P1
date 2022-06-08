from os import startfile
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape
from automata import automata


print('\n','---------------------------------------------------', 'ANALIZADOR LÉXICO PARA SIMPLE C ','---------------------------------------------------')
print('MENÚ PRINCIPAL','\n')
question1=input('¿Desea iniciar el análisis léxico?'+'\n'+'Responda: si o no'+'\n')
if question1=='si': 
    #SELECCIÓN DE ARCHIVOS
    list_files= os.listdir('C:/Users/Linda Quelex/Desktop/UNIVERSIDAD 2022/(3.1) LAB LFP/PROYECTOS/taller-lfp-main/ENTRADAS')
    print('\n')
    print('Archivos disponibles: ')
    for i in range(len(list_files)):
        print('Archivo ',i,':',list_files[i])
    print('\n')
    archivoseleccionado= input('Ingrese correlativo del archivo: ')

    print('El archivo a analizar es: ', list_files[int(archivoseleccionado)]) 
    filename=list_files[int(archivoseleccionado)]   
    file = open( './ENTRADAS/'+ filename, encoding='utf-8')
    content = file.read()
    print('\n')
    print('Finalizó la carga de archivos','\n')



# funcionamiento del analizador léxico
    tokens, errs = automata(content)

    env = Environment(loader=FileSystemLoader('src/templates'),
                      autoescape=select_autoescape(['html']))

    template = env.get_template('symbol_table.html')
    html_file = open('output.html', 'w+', encoding='utf-8')
    html_file.write(template.render(tokens=tokens, errs=errs))
    html_file.close()

    startfile('output.html')
