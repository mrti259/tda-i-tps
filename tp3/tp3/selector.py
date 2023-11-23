import sys
import os

from tp3.archivos import *
from tp3.seleccion_jugadores import *

if __name__ == "__main__":
    if (len(sys.argv) != 4):
        print("Se debe indicar la ruta del archivo a analizar, la de salida y el indice del metodo a utilizar")
        print("Ejemplo python analizar.py 'entrada/100 elem.txt' 'salida/100 elem.txt' 2")
        print("Los metodos a utilizar son:")
        print("1 = Backtracking")
        print("2 = Programacion Lineal")
        print("3 = Aproximacion Bilardo")
        print("4 = Aproximacion Greedy")
        sys.exit(1)
    
    ruta_entrada = sys.argv[1]
    ruta_salida = sys.argv[2]
    metodo = sys.argv[3]
    method_dict = {1: resolver_por_backtracking,
                   2: resolver_por_programacion_lineal,
                   3: resolver_por_aproximacion_bilardo,
                   4: resolver_greedy}
    
    if metodo not in method_dict:
        print(f"Metodo {metodo} invalido")
        print("Los metodos a utilizar son:")
        print("1 = Backtracking")
        print("2 = Programacion Lineal")
        print("3 = Aproximacion Bilardo")
        print("4 = Aproximacion Greedy")
        sys.exit(1)

    convocados = method_dict[metodo](ruta_entrada)
    guardar_convocados(convocados, ruta_salida)

    print(f"La seleccion optima es: {convocados}")
