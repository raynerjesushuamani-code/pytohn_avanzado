# funciones en python
las funciones nos permiten ordenar mejor el codigo y reutilizarlo cuando sea necesario

```python
# ejemplo deseamos crear un programa en python que nos permiten sumar dos numeros
numero_uno:int=45
numero_dos:int=70
numero_tres:int=78
numero_cuatro:int=20
suma:int=numero_uno+numero_dos
suma_dos:int=numero_tres+numero_cuatro
print(suma)
print(suma_dos)
```

como hacemos reutilizable el ejercicio anterior y mas lejible.
para eso utilizaremos funciones.
la carateristica de un funcion en python es la siguiente:
1. debe comenzar con la palabra reservda `def`.
2. debe tener un nombre que de a entender que realizara la funcion
3. debera tener parametros estos estaran encerrados en `()` no todas las funciones resistiran parametros aun asi debera tener los `()`
4. las funciones deberan retornar datos atraves de la palabra reservada `return`

```python
# crear un programa que me permita sumar dos numeros
def sumar(a,b):
    return a+b

print(sumar(78,56))
print(sumar(45,5))
```

**argumentos parametros**
**parametros** - los parametros son las variablss que se decllaran en la definicion de la, funcion 
**argumentos** -  es el dato concreto enviado en el llamado de la funciones 
**nota** en ambos casos tenemos los posicionales/nomenales

```python
# parametros
def suma(a,b): # ene ste caso tenmos una funcion sumna que recibe dos parametros a,b
suma(34,45)# en este casoo estoy llamdolo a la funcion como argumento los dato
# en este caso en concreto podemos decir que estamos fernte a una funcion que tiene parametros posicionales eso significa qu remplazara en el, orden que l pasemso a las variables 34 ->a y 45=B
def login(usuario=" pasword"==)

```
## las funciones anonimas lambda 
 las funcioens tienen las siguientes propiedades se escriben en una unica sentencia (lineal) 
 2 no tiene nombre (anonima)
 3 su cuerpo conlleva un `return` implicito 
 4 puede recibir cualquier numero de parametro 

 la estructura para definir una funcion landa es la siguiente:
 1 escribir la palabra  reservada `lambda ` 
 2 especificar la cantida de parametros 
 3 luego indicar los datos de retorno 
 4 >[TIP] puesto qeue sta funcion es anonima para ejecutarla debemos almacenar la funcion en una variable
 ```python
lambda a,b: a+b 
 
 
 ```python
 suma=lambda a,b: a+b 
 suma(3,6)
 ```
 ## dOCUMENTACION
python nos permite documentar una funcion con el objetivo de explicar mejor determinadas zonas de nuestro codigo, para esto uzamos una cadena de texto despues de la difinicion de una funcion, a esta cadena de texrto se le conoce como docstring y esta delimitado por triples comillas """aqui el texto"""

def suma(a,b):
    """
    funcion para realizar la suma de dos numeros
    """
# los docstring tambien nos permite explixcvar los parametros que recibe los datos de salida
```python
def resta(a,b):
    """
    a= un numero entero.
    b= un numero entero.
    en ambos casos a,b deben recibir valores menores 0.
    retronara un dato entero <int> positivo
    """
    return a-b
```

[!WARNING] en el proceso de documentacion tener en cuenta de incluir a lop menos lo siguiente: 
1. breve explicacion sobre que hace la funcion 
2. especificaciones y caracteristicas de los parametros incluyendo sus tipos . 
3. restricciones de la funcion. 
4. el valor que retorna y sus caracteristicas

## type this 
nos permite inidcar que tiposnde datos recibira una variablr parametro y el valor de retorno de una funcion 
para utilizarlos debemos indicar el tipo de datos despues del separador `:` en eñ caso del valor del retorno usaremos `->` luego el tipo de dato y finalmente el separador `:` que inidca el incio del bloque de codigo de la funcion 
las `anotaciones de tipo ` son una herramientas que nos permite complementar la documentacion de nuestro codigo
**tenemos los siguinentes**
**simple**
- int-> numeros enteros
- float ->numeros decimales
- boll -> datos veerdad o falso
- str-> dato de tipo texto
- lis-> listas`[]`
- tuple-> tuplas`()`
 - dic-> diccionarios`{}`

**compuesto**
existe casos en los que necesitamos mas expresividad en la *anotacion de tipos* ¿ que ocurre si queremos indicar una *lista de cadenas* o un *conjuntos de neteros*.?
- -list[str]-> lista cadna de textos
- list[in]-> lista de numeros enteros
- dict[str,float]-> diccionario donde las claves son cadenas de texto y los valores son flotantes/decimales

**multiples**
en el caso que queramos indicar  que un determinado parametro ser de un `tipo o otro` tenemos que especificarlo usando el operador `|`
- tuple|dict -> puede sert dato de tipo tupla o diccionarios 
- list [str|int] -> lista cuyos elementos pueden ser cadena de texto o enteros 
- dict[str|int,float|int] -> 

