import sys
import os

from tp1.manejo_archivos_analisis import *
from tp1.tiempo_optimo import tiempo_optimo

if __name__ == "__main__":

    if (len(sys.argv) != 3):
        print("Se debe indicar la ruta del archivo a analisar y la de salida")
        print("Ejemplo python analizar.py 'entrada/100 elem.txt' 'salida/100 elem.txt' ")
        sys.exit(1)
    
    path_entrada = sys.argv[1]
    path_salida = sys.argv[2]

    tiempos_analisis = leer_archivo_analisis(path_entrada)
    fin_de_analisis, tiempos_ordenados = tiempo_optimo(tiempos_analisis)
    escribir_archivo_analisis(tiempos_ordenados, path_salida)

    contrincantes = len(tiempos_analisis)
    print(f"El tiempo óptimo para analizar {contrincantes} contrincantes es: {fin_de_analisis}")
