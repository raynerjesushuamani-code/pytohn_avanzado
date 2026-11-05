# haciendo uso de una funcion land crear una funion que muetre un mensaje personalizado 
mensaje = lambda nombre: print(f"Hola, {nombre} Bienvenido al programa.")
mensaje("eduardo")

# crear una funcion para calcuar el area de un rectangulo sinedo la formula la siguiente area=base x altura 
area = lambda   base,altura: base *altura
base=float(input("ingrse la base del rectangulo"))
altura=float(input("ingrse la altura del rectangulo"))
print("El área del rectángulo es:", area(base, altura))

# crear una funcion que verificque si un numero es par o impar
# Crear una función lambda para verificar si es par o impar
verificar = lambda numero: "Es par" if numero % 2 == 0 else "Es impar"
numero = int(input("Ingrese un número: "))
print(verificar(numero))
