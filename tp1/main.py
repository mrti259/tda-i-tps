import sys

from tp1.leer_archivo import leer_archivo
from tp1.tiempo_optimo import tiempo_optimo

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Debe indicar un archivo con los datos de análisis.")
        sys.exit(1)
    
    path = sys.argv[1]
    tiempos_analisis = leer_archivo(path)
    fin_de_analisis = tiempo_optimo(tiempos_analisis)
    contrincantes = len(tiempos_analisis)
    print(f"El tiempo óptimo para analizar {contrincantes} contricantes es: {fin_de_analisis}")
