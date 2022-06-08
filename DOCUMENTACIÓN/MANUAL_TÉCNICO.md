# MANUAL TÉCNICO 
* Proyecto 1
* Laboratorio de Lenguajes Formales de Programación 
* Linda Madelin Fabiola Quelex Sep
* 201403745


# Ejemplo de código fuente

```Simple C
```


# Lexemas
- //
- /*línea 1 comentario
    línea 2 comentario"!"#
    línea 3 comentario*****////
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

| Token                 | Descripción                            | Patrón                           |
| --------------------- | -------------------------------------- | -------------------------------- |
| reservada_public      | Palabra reservada                      | public                           |
| reservada_class       | Palabra reservada                      | class                            |
| identificador         | Cualquier identificador del lenguaje   | (_\|[a-zA-Z])(_\|[a-zA-Z0-9])    |
| llave_abierta         | Llave abierta                          | {                                |
| llave_cerrada         | Llave cerrada                          | }                                |
| reservada_private     | Palabra reservada                      | private                          |
| reservada_final       | Palabra reservada                      | final                            |
| tipo_int              | Tipo de dato entero                    | int                              |
| operador_igual        | Operador de asignación                 | =                                |
| Dato_int              | Dato tipo entero                       | ^\d+$                            |
| punto_coma            | Punto y coma                           | ;                                |
| reservada_static      | Palabra reservada                      | static                           |
| reservada_void        | Palabra reservada                      | void                             |
| parentesis_abierto    | Paréntesis abierto                     | (                                |
| parentesis_cerrado    | Paréntesis cerrado                     | )                                |
| tipo_string           | Tipo de dato String                    | String                           |
| corchete_open         | Corchete abierto                       | [                                |
| corchete_close        | Corchete cerrado                       | ]                                |
| iterativo             | Ciclo while                            | While                            |
| menor_que             | Operador menor que                     | <                                |
| punto                 | Operador                               | .                                |
| suma                  | Operador suma                          | +                                |
| dato_String           | Dato tipo String                       | "([^"]\|(\"))*"                  |
| aaaaaaaaaaaaaaaaaaa   | aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa | aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa |
| comentario_simple     | Línea de comentario simple             | //                               |
| comentario_var_líneas | Comentario de varias líneas            | /*                               |
| tipo_Int              | Tipo de dato entero                    | (I                               | i)(N    | n)(T | t)   |
| tipo_Double           | Tipo de dato decimal                   | (D                               | d)(O    | o)(U | u)(B | b)(L | l)(E | e)   |
| tipo_String           | Tipo de dato String                    | (S                               | s)(T    | t)(R | r)(I | i)(N | n)(G | g)   |
| tipo_Char             | Tipo de dato Char                      | (C                               | c)(H    | h)(A | a)(R | r)   |
| tipo_Boolean          | Tipo de dato Boolean                   | (B                               | b)(O    | o)(O | o)(L | l)(E | e)(A | a)(N | n) |
| suma                  | Operador suma                          | +                                |
| resta                 | Operador resta                         | -                                |
| multiplicacion        | Operador multiplicación                | *                                |
| division              | Operador división                      | /                                |
| resto                 | Operador resto                         | %                                |
| igualacion            | Operador igualación                    | ==                               |
| diferenciacion        | Operador diferenciación                | !=                               |
| mayor_que             | Operador mayor que                     | >                                |
| mayor_o_igual_que     | Operador mayor o igual que             | >=                               |
| menor                 | Operador menor que                     | <                                |
| menor_o_igual_que     | Operador menor o igual que             | <=                               |
| and                   | Operador and                           | &&                               |
| or                    | Operador or                            |                                  |         |      |
| not                   | Operador not                           | !                                |
| punto_coma            | Punto y coma                           | ;                                |
| condicional           | Condicional                            | (I                               | i)(F    | f)   |
| par_abierto           | Paréntesis abierto                     | (                                |
| par_cerrado           | Paréntesis cerrado                     | )                                |
| dato_tipo_Int         | Dato tipo Int                          | ^\d+$                            | revisar |
| identificador         | Cualquier identificador del lenguaje   | (_\|[a-zA-Z])(_\|[a-zA-Z0-9])    | revisar |
| llave_abierta         | Llave abierta                          | {                                |
| llave_cerrada         | Llave cerrada                          | }                                |
| condicional_else      | Condicional else                       | (E                               | e)(L    | l)(S | s)(E | e)   |
| iterativo_while       | Iteración con ciclo while              | (W                               | w)(H    | h)(I | i)(L | l)(E | e)   |
| iterativo_do          | Iteración con ciclo do while           | (D                               | d)(O    | o)   |
| reservada_void        | Palabra reservada                      | void                             |
| reservada_return      | Retorno                                | (R                               | r)(E    | e)(T | t)(U | u)(R | r)(N | n)   |
| dato_int |
| dato_double |
| dato_string |
| dato_char |
| dato_boolean  |



- dato1_
- _datos2
- 
- (parametro,)*
 67;
Double Dato_double  =39.87;
String dato_String1= "Hola mundo";
Char _Dato_tipo__Char1 = 'a';
Boolean _ = true;
Boolean B= True;
















# Análisis léxico tarea

| Lexema             | Token              |
| ------------------ | ------------------ |
| public             | reservada_public   |
| class              | reservada_class    |
| Tarea2             | identificador      |
| {                  | llave_abierta      |
| private            | reservada_private  |
| final              | reservada_final    |
| int                | tipo_int           |
| REPETICIONES       | identificador      |
| =                  | operador_igual     |
| 5                  | Dato_int           |
| ;                  | punto_coma         |
| public             | reservada_public   |
| static             | reservada_static   |
| void               | reservada_void     |
| main               | identificador      |
| (                  | parentesis_abierto |
| String             | tipo_string        |
| [                  | corchete_open      |
| ]                  | corchete_close     |
| args               | identificador      |
| )                  | parentesis_cerrado |
| {                  | llave_abierta      |
| int                | tipo_int           |
| i                  | identificador      |
| =                  | operador_igual     |
| 0                  | Dato_int           |
| ;                  | punto_coma         |
| while              | iterativo          |
| (                  | parentesis_abierto |
| i                  | identificador      |
| <                  | menor_que          |
| REPETICIONES       | identificador      |
| )                  | parentesis_cerrado |
| {                  | llave_abierta      |
| System             | identificador      |
| .                  | punto              |
| out                | identificador      |
| .                  | punto              |
| println            | identificador      |
| (                  | llave_abierta      |
| " Repetición NO. " | dato_String        |
| +                  | suma               |
| (                  | llave_abierta      |
| i                  | identificador      |
| +                  | suma               |
| 1                  | Dato_int           |
| )                  | parentesis_cerrado |
| )                  | parentesis_cerrado |
| ;                  | punto_coma         |
| i                  | identificador      |
| +                  | suma               |
| +                  | suma               |
| ;                  | punto_coma         |
| }                  | llave_cerrada      |
| }                  | llave_cerrada      |
| }                  | llave_cerrada      |
