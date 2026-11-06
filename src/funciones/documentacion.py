# en la sigiente funcion deberan escribir la documentacion segun la convencion para el docs strings de funciones
def area_rectangulo(b,h):
    """
    funcion para calcular el area del rectangulo

    Args:
        b(int|float): este argumento sera la base del rectangulo
        h(int|float): este argumento sera la altura del rectangulo

    restriccion:
        los argumentos no podran ser igual o menores a 0

    returns:
        int|float: el resultado de la operacion b*h 
        (base*altura)            
    """
    return b*h 

# funcion para hallar la potencia de un numero
def potencia(n:int,p:int)->int:
    """
    funcion de potencia 2^3

    Args:
        n (int): numero principal-
        p (int): potencia del numero principal

    Returns:
        int: resultado del numero base potenciado 👍
    """
    resultado:int=1
    for _ in range(p):
        resultado *= n
    return resultado     
   