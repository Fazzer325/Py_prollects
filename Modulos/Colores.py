def todos():
    print("\033[30m" + "negro,", "\033[31m" + "rojo,", "\033[92m" + "verde,", "\033[93m" + "amarillo,",
          "\033[34m" + "azul,", "\033[35m" + "magenta,", "\033[36m" + "cyan,", "\033[97m" + "blanco,",
          "\033[0m" + "normal")


# -----------------------------

def negro(texto):
    pintar = "\033[30m" + texto + "\033[0m"
    return pintar


# -----------------------------

def rojo(texto):
    pintar = "\033[31m" + texto + "\033[0m"
    return pintar


# -----------------------------

def verde(texto):
    pintar = "\033[92m" + texto + "\033[0m"
    return pintar


# -----------------------------

def amarillo(texto):
    pintar = "\033[93m" + texto + "\033[0m"
    return pintar


# -----------------------------

def azul(texto):
    pintar = "\033[34m" + texto + "\033[0m"
    return pintar


# -----------------------------

def magenta(texto):
    pintar = "\033[35m" + texto + "\033[0m"
    return pintar


# -----------------------------

def cian(texto):
    pintar = "\033[36m" + texto + "\033[0m"
    return pintar


# -----------------------------

def blanco(texto):
    pintar = "\033[97m" + texto + "\033[0m"
    return pintar


# -----------------------------

def normal(texto):
    pintar = "\033[0m" + texto
    return pintar


# -----------------------------

def menu(texto):
    print("Palabra: ",texto)
    print("Menu")
    print("1° Negro")
    print("2° Rojo")
    print("3° Verde")
    print("4° Amarillo")
    print("5° Azul")
    print("6° Magenta")
    print("7° Cian")
    print("8° Blanco")
    print("9° default")
    opc = int(input("Elije una opcion: "))
    if opc == 1:
        pintar = "\033[30m" + texto + "\033[0m"
        return pintar
    elif opc == 2:
        pintar = "\033[31m" + texto + "\033[0m"
        return pintar
    elif opc == 3:
        pintar = "\033[92m" + texto + "\033[0m"
        return pintar
    elif opc == 4:
        pintar = "\033[93m" + texto + "\033[0m"
        return pintar
    elif opc == 5:
        pintar = "\033[34m" + texto + "\033[0m"
        return pintar
    elif opc == 6:
        pintar = "\033[35m" + texto + "\033[0m"
        return pintar
    elif opc == 7:
        pintar = "\033[36m" + texto + "\033[0m"
        return pintar
    elif opc == 8:
        pintar = "\033[97m" + texto + "\033[0m"
        return pintar
    elif opc == 9:
        pintar = "\033[0m" + texto
        return pintar
