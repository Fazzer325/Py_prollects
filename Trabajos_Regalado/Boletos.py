import random
from Modulos.guarda_pick import cargar,guardar

try:
    Boletos=cargar("Boletos.pkl")
    cantidad_NB=cargar("cantidad_NB.pkl")
    print("!!-Archivos Cargados-!!\n")
except:
    Boletos=[]
    print("!!-No hay un guardado-!!\n")

opc=0
numeros=[]
while opc!=4:
    print("\n1° Mostrar voletos vigentes\n2° Verificar boleto\n3° Imprimir nuevos Boletos\n4° Salir")
    opc=int(input("Elije una opcion: "))

    if opc==1:
        for el in range(len(Boletos)):
            print(f"{el+1}° Boleto {Boletos[el]}")

    elif opc==2:
        veri=[]
        print("Ingresa los numeros de el boleto de 1 en uno :")
        for el in range(cantidad_NB):
            numero=int(input(f"{el+1}° Numero : "))
            veri.append(numero)
        for el in range(len(Boletos)):
            if veri==Boletos[el]:
                print("El Boleto es valido\n")
                veri=True
            else:
                None
        if veri!=True:
            print("El Boleto no es Valido\n")

    elif opc == 3:
        numeros = []
        cantidad_Num = int(input("¿Cuántos números se podrán usar?: "))

        for el in range(cantidad_Num):
            numero = int(input(f"Ingresa el {el + 1}° Número: "))
            numeros.append(numero)

        cantidad_B = int(input("\n¿Cuántos Boletos necesitas?: "))
        cantidad_NB = int(input("\n¿Cuántos Números tendrá el boleto?: "))

        if cantidad_NB > len(numeros):
            print("Error: La cantidad de números por boleto no puede ser mayor que la cantidad de números disponibles.")

        elif cantidad_NB <= 0:
            print("Error: La cantidad de números por boleto debe ser mayor que cero.")

        else:
            Boletos = []
            for _ in range(cantidad_B):
                nums_B = random.sample(numeros, len(numeros))
                if len(nums_B) < cantidad_NB:
                    numeros_adicionales = random.sample([i for i in range(1, 100) if i not in numeros],cantidad_NB - len(nums_B))
                    nums_B.extend(numeros_adicionales)
                nums_B = nums_B[:cantidad_NB]
                random.shuffle(nums_B)
                Boletos.append(nums_B)

            guardar(Boletos, "Boletos.pkl")
            guardar(cantidad_NB, "cantidad_NB.pkl")
            print(f"{cantidad_B} boletos han sido generados y guardados.")