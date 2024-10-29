Turnos_Libreria={
    "Matutino":{
        "Matematica":0,
        "Fisica":0,
        "Quimica":0
    },
    "Vespertino":{
        "Matematica":0,
        "Fisica":0,
        "Quimica":0
    },
    "Noscturno":{
        "Matematica":0,
        "Fisica":0,
        "Quimica":0
    }
}

for el in Turnos_Libreria:
    for i in Turnos_Libreria[el]:
        Turnos_Libreria[el][i]= int(input(f"Ingresa el numero para {el} de libros de {i}:"))
    print()

suma_Mat=0; suma_Fis=0; suma_Quim=0
for el in Turnos_Libreria:
    suma_Mat += Turnos_Libreria[el]["Matematica"]
    suma_Fis += Turnos_Libreria[el]["Fisica"]
    suma_Quim += Turnos_Libreria[el]["Quimica"]
print(f"Libros Vendidos\nMatematica: {suma_Mat}\nFisica: {suma_Fis}\nQuimica: {suma_Quim}\n")

suma_Matu=0; suma_Ves=0; suma_Noc=0
for materia, cantidad in Turnos_Libreria["Matutino"].items():
    suma_Matu += cantidad
for materia, cantidad in Turnos_Libreria["Vespertino"].items():
    suma_Ves += cantidad
for materia, cantidad in Turnos_Libreria["Noscturno"].items():
    suma_Noc += cantidad

print(f"Libros comprados por turno: \nMatutino: {suma_Matu}\nVespertino: {suma_Ves}\nNocturno: {suma_Noc}\n")

suma_total=0
for el in Turnos_Libreria:
    for materia, cantidad in Turnos_Libreria[el].items():
        suma_total += cantidad

print(f"Suma total de libros vendidos en el turno Matutino: {suma_total}")