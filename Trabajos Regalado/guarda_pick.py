import pickle

def guardar(variable,nombre=None):
    try:
        if nombre==None:
            fichero = open(input("Nombre de el archivo a guardar: "), "wb")
        else:
            fichero = open(nombre, "wb")

        pickle.dump(variable, fichero)
        fichero.close()
        print("Guardado Completado")
    except:
        print("--!!No se encontro el archibo!!--")

def cargar(archivo=None):
    try:
        if archivo == None:
            fichero = open(input("Nombre de el archivo a cargar: "), "rb")
        else:
            fichero = open(archivo, "rb")

        variable = pickle.load(fichero)
        return variable
    except:
        print("--!!No se encontro el archibo!!--")