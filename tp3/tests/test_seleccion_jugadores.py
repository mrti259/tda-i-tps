import pytest

from tp3.seleccion_jugadores import *

def _assert_es_solucion_optima(convocados, cantidad_esperada):
    assert len(convocados) == cantidad_esperada

def test_backtracking():
    _assert_es_solucion_optima(resolver_por_backtracking("examples/5.txt"), 2)

def test_programacion_lineal():
    _assert_es_solucion_optima(resolver_por_programacion_lineal("examples/5.txt"), 2)