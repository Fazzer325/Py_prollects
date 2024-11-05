import itertools
import random

def generar_permutaciones_aleatorias(lista, n):
    seleccionados = random.sample(lista, n)
    permutaciones = itertools.permutations(seleccionados)
    return [''.join(map(str, p)) for p in permutaciones]

caracteres = []
rep=int(input("Ingresa La cantidad de Signos a usar: "))
for el in range(rep):
    signo=str(input(f"Ingresa el {el+1}° signo a usar: "))
    caracteres.append(signo)

cant=int(input("Ingresa la cantidad de digitos que se usaran: "))
resultado = generar_permutaciones_aleatorias(caracteres, cant)
print(resultado)

print(len(resultado), "Permutaciones")