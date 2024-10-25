from Modulos.Colores import *
from guarda_pick import guardar, cargar

print("Lista de nombres en colores\nIngresa 'end' para terminar ")
lista=[]

while True:
    nom=str(input("Ingrese Nombre: "))
    if nom=="end":
        break
    nom=menu(nom)
    lista.append(nom)

for el in lista:
    print(el)

guardar(lista,"nombres")



