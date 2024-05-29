import sys
import time
import random
from busqueda_binaria import busqueda_binaria
from busqueda_lineal import busqueda_lineal

lista = []

for i in range(10):
    lista.append(random.randint(1,59))

print(lista)

objetivo = 3

# con la dependencia time se calcula el tiempo
inicio_busqueda_lineal = time.time()

busqueda_lineal(lista, objetivo)

final_busqueda_lineal = time.time()
#resto los tiempo para obtener el tiempo que tomo de ejecución 
tiempo_busqueda_lineal =  final_busqueda_lineal - inicio_busqueda_lineal
#rcalculo la memoria utilizada
memoria_busqueda_lineal = sys.getsizeof(lista) + sys.getsizeof(objetivo)

inicio_busqueda_binaria = time.time()

busqueda_binaria(lista, objetivo)

final_busqueda_binaria = time.time()
#resto los tiempo para obtener el tiempo que tomo de ejecución 
tiempo_busqueda_binaria =  final_busqueda_binaria - inicio_busqueda_binaria

memoria_busqueda_binaria = sys.getsizeof(lista) + sys.getsizeof(objetivo)

#imprimo los resultados.
print(f"Busqueda lineal: {tiempo_busqueda_lineal} y recursos utilizados {memoria_busqueda_lineal}" )
print(f"Busqueda Binaria_: {tiempo_busqueda_binaria} y recursos utilizados {memoria_busqueda_binaria}")