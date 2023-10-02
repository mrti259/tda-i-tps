import sys
import os

from tp2.archivos import *
from tp2.entrenamiento import *

if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print("Se debe indicar la ruta del archivo a analizar y la de salida")
        print("Ejemplo python analizar.py 'entrada/100 elem.txt' 'salida/100 elem.txt' ")
        sys.exit(1)
    
    ruta_entrada = sys.argv[1]
    ruta_salida = sys.argv[2]

    datos = leer_archivo(ruta_entrada)
    ganancia, plan = mejor_ganancia(*datos)
    guardar_plan_de_entrenamiento(plan, ruta_salida)

    print(f"La ganancia óptima es: {ganancia}")
