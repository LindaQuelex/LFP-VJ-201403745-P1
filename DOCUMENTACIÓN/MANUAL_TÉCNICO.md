# MANUAL TÉCNICO 
* Proyecto 1
* Laboratorio de Lenguajes Formales de Programación 
* Linda Madelin Fabiola Quelex Sep
* 201403745


# Ejemplo de código fuente

```Simple C
// comentario de una línea

/*
Comentario
De varias
Líneas
*/

Int _dato_int = 67;
Double Dato_double  =39.87;
String dato_String1= "Hola mundo";
Char _Dato_tipo__Char1 = 'a';
Boolean _ = true;
Boolean B= True;
```

# Lexemas
- // comentario 1 línea sdri0werw023"#"#" 
- /*línea 1 comentario
    línea 2 comentario"!"#
    línea 3 comentario
   */
- Int
- Double
- String
- Char
- Boolean
- +
- -
- *
- /
- %
- ==
- !=
- >
- >=
- <
- <=
- &&
- ||
- !
- ;
- if 
- (
- dato1_
- _datos2
- )
- {
- }
- else
- while
- do
- void
- (parametro,)*
- return


# Definición de tokens

| Token                 | Descripción                          | Patrón              |
| --------------------- | ------------------------------------ | ------------------- |
| comentario_simple     | Línea de comentario simple           | ^\/\/.*\n           |
| comentario_var_líneas | Comentario de varias líneas          | (\/\*(\s*|.*?)*\*\/)|(\/\/.*)  |
| tipo_int              | Tipo de dato entero                  | int                 |
| tipo_double           | Tipo de dato decimal                 | double              |
| tipo_string           | Tipo de dato String                  | string              |
| tipo_char             | Tipo de dato Char                    | char                |
| tipo_boolean          | Tipo de dato boolean                 | boolean             |
| suma                  | Operador suma                        | +                   |
| resta                 | Operador resta                       | -                   |
| multiplicacion        | Operador multiplicación              | *                   |
| division              | Operador división                    | /                   |
| resto                 | Operador resto                       | %                   |
| igualacion            | Operador igualación                  | ==                  |
| diferenciacion        | Operador diferenciación              | !=                  |
| mayor_que             | Operador mayor que                   | >                   |
| mayor_o_igual_que     | Operador mayor o igual que           | >=                  |
| menor_que             | Operador menor que                   | <                   |
| menor_o_igual_que     | Operador menor o igual que           | <=                  |
| and                   | Operador and                         | &&                  |
| or                    | Operador or                          | \|\|                |
| not                   | Operador not                         | !                   |
| punto_coma            | Punto y coma                         | ;                   |
| condicional           | Condicional                          | if                  |
| par_abierto           | Paréntesis abierto                   | (                   |
| par_cerrado           | Paréntesis cerrado                   | )                   |
| dato_tipo_Int         | Dato tipo Int                        | ^\d+$               |
| identificador         | Cualquier identificador del lenguaje | _|[a-zA-Z]([a-zA-Z0-9]*)_*  |
| llave_abierta         | Llave abierta                        | {                   |
| llave_cerrada         | Llave cerrada                        | }                   |
| condicional_else      | Condicional else                     | else                |
| iterativo_while       | Iteración con ciclo while            | while               |
| iterativo_do          | Iteración con ciclo do while         | do                  |
| reservada_void        | Palabra reservada                    | void                |
| reservada_return      | Retorno                              | return              |
| dato_int              | Dato tipo entero                     | [0-9]+
| dato_double           | Dato tipo double                     | [+-]?[0-9]+\.[0-9]+ |
| dato_string           | Datos tipo String                    | "([^"]\|(\"))*.*"   |
| dato_char             | Dato tipo char                       |                     | definir                  |
| dato_boolean          | Dato tipo boolean                    | true|false          |
| parametro             | Parámetro                            | \(.*\,\)\*          |



Char _Dato_tipo__Char1 = 'a';


# Análisis léxico

| Lexema                                                        | Token                 |
| ------------------------------------------------------------- | --------------------- |
| // comentario 1 línea sdri0werw023"#"#"                       | comentario_simple     |
| /*línea 1 comentario línea 2 comentario línea 3 comentario */ | comentario_var_líneas |
| Int                                                           | tipo_int              |
| Double                                                        | tipo_double           |
| String                                                        | tipo_string           |
| Char                                                          | tipo_char             |
| Boolean                                                       | tipo_boolean          |
| +                                                             | suma                  |
| -                                                             | resta                 |
| *                                                             | multiplicacion        |
| /                                                             | division              |
| %                                                             | resto                 |
| ==                                                            | igualacion            |
| !=                                                            | diferenciacion        |
| >                                                             | mayor_que             |
| >=                                                            | mayor_o_igual_que     |
| <                                                             | menor_que             |
| <=                                                            | menor_o_igual_que     |
| &&                                                            | and                   |
| \/\/                                                          | or                    |
| !                                                             | not                   |
| ;                                                             | punto_coma            |
| if                                                            | condicional           |
| (                                                             | par_abierto           |
| dato1_                                                        | identificador         |
| _datos2                                                       | identificador         |
| )                                                             | par_cerrado           |
| {                                                             | llave_abierta         |
| }                                                             | llave_cerrada         |
| else                                                          | condicional_else      |
| while                                                         | iterativo_while       |
| do                                                            | iterativo_do          |
| void                                                          | reservada_void        |
| (parametro,)*                                                 | parametro             |
| return                                                        | reservada_return      |

# Conversión de expresión regular a AFD a través del método del árbol 

