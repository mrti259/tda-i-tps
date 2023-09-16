import os

def escribir_archivo_analisis(contenido, path):
    base_path = os.path.dirname(path)
    os.makedirs(base_path, exist_ok=True)
    with open(path, 'w') as archivo:
        archivo.write("S_i,A_i\n")

        for tiempo_analisis in contenido:
            archivo.write(f"{tiempo_analisis[0]},{tiempo_analisis[1]}\n")

def leer_archivo_analisis(path):
    tiempos_analisis = []
    with open(path) as archivo:
        encabezado = archivo.readline()
        for linea in archivo.readlines():
            tiempo_scaloni, tiempo_ayudante = linea.split(",")
            tiempos_analisis.append((int(tiempo_scaloni), int(tiempo_ayudante)))
    return tiempos_analisis