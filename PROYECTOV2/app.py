import os



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
    file = open( './ENTRADAS/'+ list_files[int(archivoseleccionado)] , encoding='utf-8')
    content = file.read()
    print('\n')
    print('Finalizó la carga de archivos','\n')
