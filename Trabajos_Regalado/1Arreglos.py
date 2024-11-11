estudiantes = [
    ["Alice", 20, [8, 9, 8],True],
    ["Bob", 22, [7, 3, 6],False],
    ["Charlie", 21, [9, 10, 9],True],
]
def mostrar_estudiantes(estudiantes):
    for estudiante in estudiantes:
        nombre = estudiante[0]
        edad = estudiante[1]
        calificaciones = estudiante[2]
        aprovado = estudiante[3]
        promedio = sum(calificaciones) / len(calificaciones)
        print(f"Nombre: {nombre}, Edad: {edad}, Promedio de Calificaciones: {promedio:.1f}, Esta Aprovado?: {"Si" if aprovado else "No"}")

mostrar_estudiantes(estudiantes)