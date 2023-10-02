import pytest
import os
import time

from tp2.entrenamiento import *
from tp2.archivos import leer_archivo

RUTA_EJEMPLOS = "examples"

def assert_mejor_ganancia(esperado, datos):
    assert esperado == mejor_ganancia(*datos)[0]
    # assert esperado == mejor_ganancia_greedy(*datos)
    # assert esperado == mejor_ganancia_recursivo(*datos)
    # assert esperado == mejor_ganancia_recursivo_con_memoria(*datos)
    # assert esperado == mejor_ganancia_iterativo(*datos)

def test_1():
    # dias = 0
    ganancia_por_dia = []
    energia_por_dia = []
    assert_mejor_ganancia(0, (ganancia_por_dia, energia_por_dia))

def test_2():
    # dias = 1
    ganancia_por_dia = [10]
    energia_por_dia = [1]
    assert_mejor_ganancia(1, (ganancia_por_dia, energia_por_dia))

def test_3():
    # dias = 1
    ganancia_por_dia = [1]
    energia_por_dia = [10]
    assert_mejor_ganancia(1, (ganancia_por_dia, energia_por_dia))

def test_4():
    # dias = 2
    ganancia_por_dia = [1, 1]
    energia_por_dia = [1, 1]
    assert_mejor_ganancia(2, (ganancia_por_dia, energia_por_dia))

def test_5():
    # dias = 2
    ganancia_por_dia = [1, 10]
    energia_por_dia = [10, 1]
    assert_mejor_ganancia(10, (ganancia_por_dia, energia_por_dia))

def test_6():
    # dias = 3
    ganancia_por_dia = [10, 10, 10]
    energia_por_dia = [10, 5, 1]
    assert_mejor_ganancia(20, (ganancia_por_dia, energia_por_dia))

def test_7():
    # dias = 3
    ganancia_por_dia = [10, 1, 100]
    energia_por_dia = [10, 5, 1]
    assert_mejor_ganancia(20, (ganancia_por_dia, energia_por_dia))

def test_8():
    # dias = 3
    ganancia_por_dia = [10, 50, 100]
    energia_por_dia = [100, 5, 1]
    assert_mejor_ganancia(110, (ganancia_por_dia, energia_por_dia))

def test_archivos():
    ejemplos = [
        ("3.txt", 7),
        ("10.txt", 380),
        ("10_bis.txt", 523),
        ("10_todo_entreno.txt", 900),
        ("50.txt", 1870),
        ("50_bis.txt", 2136),
        ("100.txt", 5325),
        ("500.txt", 27158),
        ("1000.txt", 54021),
        ("5000.txt", 279175),
    ]
    for archivo_ejemplo, ganancia_esperada in ejemplos:
        print(f"Testeando archivo {archivo_ejemplo}")
        ruta = os.path.join(RUTA_EJEMPLOS, archivo_ejemplo)
        datos = leer_archivo(ruta)
        print(f"    Ejecutando analisis...")
        tiempo_inicio = time.perf_counter()
        assert_mejor_ganancia(ganancia_esperada, datos)
        tiempo_fin = time.perf_counter()
        print(f"    Ejecutado en {round((tiempo_fin - tiempo_inicio) * 1000, 2)} ms")