## crear una funcin que reciba 5 nmeros enteros  y retorne solo una lista de numeros  pares  tener en cuenta las anotaciones
def num_pares(a:int,b:int,c:int,d:int,e:) ->list [int]:
numeros:list[int]=[a,b,c,d,e]
numeros_pares:list[int]=[]
for i in numeros:
    if i%2==0:
        numeros_pares.append(i)
        return numeros_pares
    
