
Turnos_Libreria = {}

num_turnos = int(input("¿Cuántos turnos deseas agregar? "))
num_materias = int(input("¿Cuántas materias tienen los turnos? "))

materias = []
for _ in range(num_materias):
    materia = input(f"Ingrese el nombre de la {_ + 1}° materia: ")
    materias.append(materia)

for _ in range(num_turnos):
    turno = input(f"\nIngresa el nombre del {_ + 1}° turno: ")
    Turnos_Libreria[turno] = {}

    for materia in materias:
        horas = int(input(f"Ingrese los libros comprados de {materia} para el turno {turno}: "))
        Turnos_Libreria[turno][materia] = horas

print("\nSuma de libros vendidos por turno:")
total_general = 0
for turno, materias in Turnos_Libreria.items():
    total_libros_turno = sum(materias.values())
    total_general += total_libros_turno
    print(f"{turno}: {total_libros_turno} libros vendidos")

suma_por_materia = {materia: 0 for materia in materias}

for libros in Turnos_Libreria.values():
    for materia, cantidad in libros.items():
        suma_por_materia[materia] += cantidad

print("\nSuma de libros vendidos por materia:")
for materia, total in suma_por_materia.items():
    print(f"{materia}: {total} libros vendidos")

print(f"\nTotal de libros vendidos: {total_general} libros")

print("\nProbabilidad de que un libro sea comprado por materia:")
for materia, total in suma_por_materia.items():
    probabilidad_materia = total / total_general if total_general > 0 else 0
    print(f"{materia}: {probabilidad_materia:.1%} de probabilidad")

print("\nProbabilidad de que un libro sea comprado por turno:")
for turno, libros in Turnos_Libreria.items():
    total_libros_turno = sum(libros.values())
    probabilidad_turno = total_libros_turno / total_general if total_general > 0 else 0
    print(f"{turno}: {probabilidad_turno:.1%} de probabilidad")

