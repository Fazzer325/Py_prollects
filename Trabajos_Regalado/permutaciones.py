import itertools
import random

def generar_permutaciones_aleatorias(lista, n):
    if n > len(lista):
        print("¡Advertencia! La cantidad de dígitos a usar es mayor que los caracteres disponibles.")
        return []
    seleccionados = random.sample(lista, n)
    permutaciones = itertools.permutations(seleccionados)
    return [''.join(map(str, p)) for p in permutaciones]


def generar_todas_las_permutaciones(lista):
    permutaciones = itertools.permutations(lista)
    return [''.join(map(str, p)) for p in permutaciones]

caracteres = []
rep = int(input("Ingresa la cantidad de signos a usar: "))

for el in range(rep):
    signo = str(input(f"Ingresa el {el + 1}° signo a usar: "))
    caracteres.append(signo)

cant = int(input("Ingresa la cantidad de dígitos que se usarán: "))
opcion = input("¿Deseas generar todas las permutaciones (s/n)? ")
if opcion.lower() == 's':
    resultado = generar_todas_las_permutaciones(caracteres)
else:
    resultado = generar_permutaciones_aleatorias(caracteres, cant)

print("\nPermutaciones generadas:")
print(resultado)
print(len(resultado), "Permutaciones")
