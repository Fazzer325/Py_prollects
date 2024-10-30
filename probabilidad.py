from Modulos.Colores import *
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

#Ingresa cantidad de libros comprados
for el in Turnos_Libreria:
    for i in Turnos_Libreria[el]:
        Turnos_Libreria[el][i]= int(input(amarillo(f"Ingresa el numero para {azul(el)} {amarillo("de libros de ")}{azul(i)}:")))
    print()

#Suma de libros vendidos por materia
suma_Mat=0; suma_Fis=0; suma_Quim=0
for el in Turnos_Libreria:
    suma_Mat += Turnos_Libreria[el]["Matematica"]
    suma_Fis += Turnos_Libreria[el]["Fisica"]
    suma_Quim += Turnos_Libreria[el]["Quimica"]
print(f"{cian("Libros Vendidos")}\nMatematica: {suma_Mat}\nFisica: {suma_Fis}\nQuimica: {suma_Quim}\n")

#Suma libros vendidos por turno
suma_Matu=0; suma_Ves=0; suma_Noc=0
for materia, cantidad in Turnos_Libreria["Matutino"].items():
    suma_Matu += cantidad
for materia, cantidad in Turnos_Libreria["Vespertino"].items():
    suma_Ves += cantidad
for materia, cantidad in Turnos_Libreria["Noscturno"].items():
    suma_Noc += cantidad

print((f"{cian("Libros comprados por turno: ")}\nMatutino: {suma_Matu}\nVespertino: {suma_Ves}\nNocturno: {suma_Noc}\n"))

#total de libros vendidos
suma_total=0
for el in Turnos_Libreria:
    for materia, cantidad in Turnos_Libreria[el].items():
        suma_total += cantidad

print(verde(f"Suma total de libros vendidos en total: ")+f"{suma_total}\n")

print(cian("Probabilidades De que se compre un Libro"))
print(f"Probabilidad de Que se compre un libro de Matematicas: {suma_Mat/suma_total:.1f}")
print(f"Probabilidad de Que se compre un libro de Fisica: {suma_Fis/suma_total:.1f}")
print(f"Probabilidad de Que se compre un libro de Quimica: {suma_Quim/suma_total:.1f}\n")

print(cian("Probabilidad de Que se compre un libro por turno"))
print(f"Probabilidad de Que se compre un libro en el truno Matutino: {suma_Matu/suma_total:.1f}.")
print(f"Probabilidad de Que se compre un libro en el truno Vespertino: {suma_Ves/suma_total:.1f}")
print(f"Probabilidad de Que se compre un libro en el truno Nocturno: {suma_Noc/suma_total:.1f}")
