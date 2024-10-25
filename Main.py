from Modulos.Colores import *

print(f"Mi nombre es {cian("Cristo")} y yo {verde("Soy un Programador")}")

Numeros=[1,2,3,4,5,6,7,8,9]

def suma(*Numeros):
    total=0
    for i in Numeros:
        total+=i

    print(total)

suma(*Numeros)