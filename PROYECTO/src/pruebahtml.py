from ctypes.wintypes import PINT
from os import startfile
from automata import automata

# PRUEBA SIN USAR JINJA
file_exit=input('Ingrese el nombre del archivo de salida: ')
print('\n')
file = open(file_exit+'.html','w+', encoding='utf-8')

titulopage = "REPORTES P1LFP"
lista=["mango", "pera", "sandia"]
p_inicio="<td>"
p_final= "</td>"
for frutas in lista:
    lineas=p_inicio+str(lista)+p_final
    

file2 = open( './ENTRADAS/prueba_entrada.sc', encoding='utf-8')
content = file2.read()
tokens, errs = automata(content)


mensaje = f"""<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" type="text/css" href="C:/Users/Linda Quelex/Desktop/UNIVERSIDAD 2022/(3.1) LAB LFP/PROYECTOS/PROYECTO1/LFP-VJ-201403745-P1/PROYECTO/src/style.css">
    
    <title>{titulopage}</title>
  </head>
  <body>

  <h1 style="text-align: center">REPORTES ANALIZADOR LÉXICO DE SIMPLE C</h1>
    
    <h2 style="text-align: center">REPORTE DE TOKENS</h2>
    <table>
      <thead>
        <th>Línea</th>
        <th>Columna</th>
        <th>Lexema</th>
        <th>Token</th>
        <th>Patrón</th>        
      </thead>
      <tbody>
     
        <tr>
          <td>{tokens}</td>
          {lineas}
          {lineas}
          {lineas}
          {lineas}

                        
        </tr>

      </tbody>
    </table>

    <h2 style="text-align: center">REPORTE DE AUTOMÁTA FINITO DETERMINÍSTA -AFD- </h2>
    <table>
      <thead>
        <th>Estado</th>
        <th>Caracter</th>
        <th>Lexema reconocido</th>
        <th>Siguiente estado</th>
      </thead>
      <tbody>
        
        <tr>
          <td>{{e.char}}</td>
          <td>{{e.row}}</td>
          <td>{{e.col}}</td>
        </tr>
     
      </tbody>
    </table>
  </body>
</html>

    <h2 style="text-align: center">REPORTE DE ERRORES</h2>
    <table>
      <thead>
        <th>Línea</th>
        <th>Columna</th>
        <th>Lexema</th>
      </thead>
      <tbody>
    
        <tr>
          <td>{{e.row}}</td>
          <td>{{e.col}}</td>
          <td>{{e.char}}</td>
        </tr>
        
      </tbody>
    </table>
  </body>
</html>
"""

file.write(mensaje)
file.close()

startfile(file_exit+'.html')
startfile('output.html')