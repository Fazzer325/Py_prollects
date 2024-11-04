import random

numeros=[]
Boletos=[]

while True:
    print("\n1° Mostrar voletos vigentes\n2° Verificar boleto\n3° Imprimir nuevos Boletos\n")
    opc=int(input("Elije una opcion: "))

    if opc==1:
        for el in range(len(Boletos)):
            print(f"{el+1}°Boleto {Boletos[el]}")

    elif opc==2:
        P_B=int(input("Ingresa el numero de el boleto: "))
        for el in range(len(Boletos)):
            if range(len(P_B))!=range(len(Boletos[el])):
                print("La cantidad de numeros es difetentes")

    elif opc==3:
        cantidad_Num=int(input("Cuantos numeros se podran usar?: "))
        for el in range(cantidad_Num):
            numero=int(input(f"Ingresa el {el+1}° Numero : "))
            numeros.append(numero)

        cantidad_B = int(input("\nCuantos Boletos nesesitas?: "))
        cantidad_NB = int(input("\nCuantos Numeros tendra el boleto?: "))
        for _ in range(cantidad_B):
            nums_B = random.sample(numeros, cantidad_NB)
            Boletos.append(nums_B)


