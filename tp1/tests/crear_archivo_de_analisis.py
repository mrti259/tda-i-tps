import random

def generar_tiempo_analisis():
    return (random.randint(1, 1000000), random.randint(1, 1000000))

def crear_archivo_de_analisis(path_archivo, cantidad_contricantes):
    with open(path_archivo, 'w') as archivo:
        archivo.write("S_i,A_i\n")

        for _ in range(cantidad_contricantes):
            tiempo_analisis = generar_tiempo_analisis()
            archivo.write(f"{tiempo_analisis[0]},{tiempo_analisis[1]}\n")
