
import pytest

import os
import time
import re

from tp2.entrenamiento import mejor_ganancia
from tp2.archivos import leer_archivo

RUTA_EJEMPLOS = "examples"

def test_ejemplos():
    datos_de_prueba = []

    with open("notebooks/Resultados Esperados.txt") as archivo:
        contenido = archivo.readlines()
        for i in range(0, len(contenido), 4):
            nombre_archivo_analisis = contenido[i].strip()
            ganancia_esperada = int(re.search("Ganancia maxima: (\d+)", contenido[i+1]).groups(0)[0])
            plan_esperado = re.search("Plan de entrenamiento: ([^\n]+)", contenido[i+2]).groups(0)[0].split(", ")
            plan_entrenamiento_normalizado = [(1 if estrategia == "Entreno" else 0) for estrategia in plan_esperado]
            datos_de_prueba.append((nombre_archivo_analisis, ganancia_esperada, plan_entrenamiento_normalizado))
    
    for nombre_archivo_analisis, ganancia_esperada, plan_esperado in datos_de_prueba:
        print(f"Testeando archivo {nombre_archivo_analisis}")
        datos = leer_archivo(os.path.join(RUTA_EJEMPLOS, nombre_archivo_analisis))

        print(f"    Ejecutando analisis...")
        tiempo_inicio = time.perf_counter()
        ganancia_obtenida, plan_obtenido = mejor_ganancia(*datos)
        tiempo_fin = time.perf_counter()
        print(f"    Ejecutado en {round((tiempo_fin - tiempo_inicio) * 1000, 2)} ms")

        assert ganancia_esperada == ganancia_obtenida
        for i in range(len(plan_esperado)):
            assert plan_esperado[i] == plan_obtenido[i]