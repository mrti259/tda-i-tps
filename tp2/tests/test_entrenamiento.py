import pytest

from tp2.entrenamiento import *

def assert_mejor_ganancia(esperado, datos):
    assert esperado == mejor_ganancia(*datos)[0]
    # assert esperado == mejor_ganancia_greedy(*datos)[0]
    assert esperado == mejor_ganancia_recursivo(*datos)[0]
    assert esperado == mejor_ganancia_recursivo_con_memoria(*datos)[0]
    assert esperado == mejor_ganancia_iterativo(*datos)[0]

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