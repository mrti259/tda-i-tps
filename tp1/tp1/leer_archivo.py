def leer_archivo(path):
    datos = []
    with open(path) as archivo:
        encabezado = archivo.readline()
        for linea in archivo.readlines():
            s_i, a_i = linea.split(",")
            datos.append((int(s_i), int(a_i)))
    return datos