Alumnos = {
    "Nombre": [
        "Juan", "María", "Pedro", "Lucía", "Carlos", "Ana", "Luis", "Sofía", "Javier", "Elena",
        "Andrés", "Marta", "Diego", "Clara", "Fernando", "Isabel", "Roberto", "Patricia", "Miguel", "Laura",
        "Antonio", "Julia", "Francisco", "Nuria", "David", "Sara", "Alberto", "Carmen", "Rafael", "Teresa"
    ],
    "Tareas": [
        8, 5, 7, 9, 6, 10, 4, 3, 7, 8,
        6, 0, 9, 4, 0, 7, 0, 2, 6, 3,
        9, 10, 5, 8, 7, 6, 4, 2, 9, 3
    ],
    "Trabajos": [
        7, 6, 9, 8, 10, 5, 4, 3, 8, 9,
        6, 7, 10, 8, 5, 6, 9, 2, 4, 3,
        8, 7, 10, 5, 6, 9, 10, 3, 7, 4
    ],
    "Examen": [
        10, 8, 6, 7, 9, 5, 4, 10, 6, 0,
        9, 7, 10, 0, 8, 5, 3, 4, 10, 6,
        9, 7, 8, 5, 4, 10, 6, 0, 9, 3
    ]
}
for el in range(len(Alumnos["Nombre"])):
    promedio = (Alumnos["Examen"][el] + Alumnos["Tareas"][el] + Alumnos["Trabajos"][el]) / 3
    print(f"\n{Alumnos["Nombre"][el]} Tiene un promedio de: {promedio}")
    if promedio < 5:
        print("!!Esta Reprobado!!")
    else:
        print("!!Esta Aprobado!!")

    if Alumnos["Examen"][el] ==0:
        print("El Alumno no hiso examen!!")
        res=str(input("Permitir al alumno hacer el examen ?: "))
        if res=="Si" or res=="si":
            print("!!--El Alumno hara el examen la siguiente clase--!! ")

    elif Alumnos["Tareas"][el] ==0:
        print("El Alumno no Entregos las tareas!!")
        res=str(input("Permitir al alumno entragar las tareas ?: "))
        if res=="Si" or res=="si":
            print("!!--El Alumno entregara las tareas la siguiente clase--!! ")