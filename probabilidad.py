Turnos_Libreria={
    "Matutino":{
        "Matematica":(10),
        "Fisica":(50),
        "Quimica":(40)
    },
    "Vespertino":{
        "Matematica":(50),
        "Fisica":(10),
        "Quimica":(5)
    },
    "Noscturno":{
        "Matematica":(5),
        "Fisica":(10),
        "Quimica":(5)
    }
}

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