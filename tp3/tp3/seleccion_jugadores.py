from tp3.archivos import leer_archivo
from tp3.algoritmos import *

def resolver_por_backtracking(archivo):
    deseos = leer_archivo(archivo)
    return hitting_set_backtracking(deseos)

def resolver_por_programacion_lineal(archivo):
    deseos = leer_archivo(archivo)
    return hitting_set_programacion_lineal(deseos)

def resolver_por_aproximacion_bilardo(archivo):
    deseos = leer_archivo(archivo)
    return hitting_set_aproximacion_bilardo(deseos)

def resolver_greedy(archivo):
    deseos = leer_archivo(archivo)
    return hitting_set_greedy(deseos)
