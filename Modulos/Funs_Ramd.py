def print_lista(lista,Texto=None):
    if Texto == None:
        for el in lista:
            print(el)
    else:
        for el in lista:
            print(f"{el} {Texto}")

def print_lista_enum(lista,Texto=None):
    if Texto is None:
        for el in range(len(lista)):
            print(f"{el+1}° {lista[el]}")
    else:
        for el in range(len(lista)):
            print(f"{el+1}° {lista[el]} {Texto}")