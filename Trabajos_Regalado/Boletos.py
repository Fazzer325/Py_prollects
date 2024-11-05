import random
from Modulos.guarda_pick import cargar, guardar
from Modulos.Colores import *

try:
    Boletos = cargar("Boletos.pkl")
    cantidad_NB = cargar("cantidad_NB.pkl")
    if Boletos is None:
        print(rojo(f"!!-No se pudo cargar los archivos-!!"))
    else:
        print("!!-Archivos Cargados-!!")
except:
    Boletos = []

opc = 0
numeros = []

while opc != 4:
    print("\n1° Mostrar boletos vigentes\n2° Verificar boleto\n3° Imprimir nuevos boletos\n4° Salir")

    try:
        opc = int(input("Elije una opción: "))
    except:
        print("Error, intenta de nuevo")
        continue

    if opc == 1:
        try:
            print("\nBoletos vigentes:")
            if len(Boletos) > 0:
                for el, boleto in enumerate(Boletos, start=1):
                    print(f"{el}° Boleto: {list(boleto)}")
            else:
                print("No hay boletos guardados.")
        except:
            print("\n!!-No hay un guardado / No se han generado boletos!!!")

    elif opc == 2:
        try:
            veri = []
            print("Ingresa los números del boleto uno por uno:")
            for el in range(cantidad_NB):
                numero = int(input(f"{el + 1}° Número: "))
                veri.append(numero)

            veri_tuple = tuple(veri)
            if veri_tuple in Boletos:
                print("El boleto es válido\n")
            else:
                print("El boleto no es válido\n")
        except:
            print("\n!!-No hay un guardado / No se han generado boletos!!!")

    elif opc == 3:
        numeros = []
        cantidad_Num = int(input("¿Cuántos números se podrán usar?: "))

        for el in range(cantidad_Num):
            numero = int(input(f"Ingresa el {el + 1}° Número: "))
            numeros.append(numero)

        cantidad_B = int(input("\n¿Cuántos boletos necesitas?: "))
        cantidad_NB = int(input("\n¿Cuántos números tendrá el boleto?: "))

        if cantidad_NB > len(numeros):
            print("Error: La cantidad de números por boleto no puede ser mayor que la cantidad de números disponibles.")
        elif cantidad_NB <= 0:
            print("Error: La cantidad de números por boleto debe ser mayor que cero.")
        else:
            i = 0
            veri = False
            Boletos = set()

            for _ in range(cantidad_B):
                nums_B = random.sample(numeros, len(numeros))
                nums_B = nums_B[:cantidad_NB]
                nums_B_tuple = tuple(nums_B)

                if nums_B_tuple in Boletos:
                    i += 1
                    if i == 2000:
                        print(f"Solo se imprimieron {len(Boletos)} boletos antes de repetirse\n")
                        veri = False
                        break
                    continue

                Boletos.add(nums_B_tuple)

            Boletos = list(Boletos)
            guardar(Boletos, "Boletos.pkl")
            guardar(cantidad_NB, "cantidad_NB.pkl")

            if veri ==False:
                print(f"{len(Boletos)} boletos han sido generados y guardados.")
            else:
                print("No se generaron boletos válidos.")
    else:
        print(rojo("\n!!-Opción no válida-!!"))

print(rojo("\n!!-Programa Finalizado-!!"))
