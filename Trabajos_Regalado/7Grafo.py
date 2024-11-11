import itertools
import random
Nodos={
    "A":0,
    "B":0,
    "C":0,
    "D":0,
    "E":0,
    "F":0,
    "G":0,
    "H":0,
    "I":0,
    "J":0
}
Suma=0
while True:
    for el in Nodos:
        Nodos[el] = random.randint(1, 9)

    claves_aleatorias = random.sample(list(Nodos.keys()), 9)
    #for i in claves_aleatorias: print(f"{i} : {Nodos[i]}")
    perms = list(itertools.permutations(claves_aleatorias))
    random.shuffle(perms)

    for el in perms[:5]:
        a=el[:5]
        print(f"{Nodos[a[0]]}    {Nodos[a[1]]}    {Nodos[a[2]]}    {Nodos[a[3]]}    {Nodos[a[4]]}")
        print(f"{a[0]}--> {a[1]}--> {a[2]}--> {a[3]}--> {a[4]}\n")

    input("Pulsa Enter para Ver Resultados: ");print()

    for el in perms[:5]:
        Suma=0
        a=el[:5]

        for i in a:
            Suma=Suma+Nodos[i]
        print(f"{Nodos[a[0]]}    {Nodos[a[1]]}    {Nodos[a[2]]}    {Nodos[a[3]]}    {Nodos[a[4]]}")
        print(f"{a[0]}--> {a[1]}--> {a[2]}--> {a[3]}--> {a[4]} : {Suma}\n")

    b=str(input("Pulsa enter para la siguiente ronda / o escribe end para terminar: "))
    if b=="end" or b=="End" or b=="END":
        break
    for el in range(20):print("")

print("!!!--Programa Finalisado--!!!")
