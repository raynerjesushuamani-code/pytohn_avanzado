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
 
 ``` 
 ```python
 suma=lambda a,b: a+b 
 suma(3,6)
 ```