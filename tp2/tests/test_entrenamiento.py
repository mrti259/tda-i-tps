import pytest
import os

from tp2.entrenamiento import mejor_ganancia
from tp2.archivos import leer_archivo

RUTA_EJEMPLOS = "examples"

def assert_mejor_ganancia(esperado, datos):
    assert esperado == mejor_ganancia(*datos)[0]

def test_1():
    dias = 0
    ganancia_por_dia = []
    energia_por_dia = []
    assert_mejor_ganancia(0, (dias, ganancia_por_dia, energia_por_dia))

def test_2():
    dias = 1
    ganancia_por_dia = [10]
    energia_por_dia = [1]
    assert_mejor_ganancia(1, (dias, ganancia_por_dia, energia_por_dia))

def test_3():
    dias = 1
    ganancia_por_dia = [1]
    energia_por_dia = [10]
    assert_mejor_ganancia(1, (dias, ganancia_por_dia, energia_por_dia))

def test_4():
    dias = 2
    ganancia_por_dia = [1, 1]
    energia_por_dia = [1, 1]
    assert_mejor_ganancia(2, (dias, ganancia_por_dia, energia_por_dia))

def test_5():
    dias = 2
    ganancia_por_dia = [1, 10]
    energia_por_dia = [10, 1]
    assert_mejor_ganancia(10, (dias, ganancia_por_dia, energia_por_dia))

def test_6():
    dias = 3
    ganancia_por_dia = [10, 10, 10]
    energia_por_dia = [10, 5, 1]
    assert_mejor_ganancia(20, (dias, ganancia_por_dia, energia_por_dia))

def test_7():
    dias = 3
    ganancia_por_dia = [10, 1, 100]
    energia_por_dia = [10, 5, 1]
    assert_mejor_ganancia(20, (dias, ganancia_por_dia, energia_por_dia))

def test_8():
    dias = 3
    ganancia_por_dia = [10, 50, 100]
    energia_por_dia = [100, 5, 1]
    assert_mejor_ganancia(110, (dias, ganancia_por_dia, energia_por_dia))

def test_archivos():
    ejemplos = [
        ("3.txt", 7),
        # ("10.txt", 380),
        # ("10_bis.txt", 523),
        ("10_todo_entreno.txt", 900),
        # ("50.txt", 1870),
        # ("50_bis.txt", 2136),
        # ("100.txt", 5325),
        # ("500.txt", 27158),
        # ("1000.txt", 54021),
        # ("5000.txt", 279175),
    ]
    for archivo_ejemplo, ganancia_esperada in ejemplos:
        ruta = os.path.join(RUTA_EJEMPLOS, archivo_ejemplo)
        datos = leer_archivo(ruta)
        assert_mejor_ganancia(ganancia_esperada, datos)