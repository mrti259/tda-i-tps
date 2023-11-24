import pytest

from tp3.archivos import leer_archivo
from tp3.algoritmos import *

def test_es_hitting_set():
    assert es_hitting_set([], [])
    assert not es_hitting_set([["Messi"]], [])
    assert es_hitting_set([["Messi"]], ["Messi"])
    assert not es_hitting_set([["Messi"], ["Dybala"]], ["Messi"])
    assert es_hitting_set([["Messi"], ["Dybala"]], ["Messi", "Dybala"])
    assert es_hitting_set([["Messi", "Di Maria"], ["Dybala", "Dibu", "Messi"]], ["Messi"])
    assert es_hitting_set([["Messi", "Di Maria"], ["Dybala", "Dibu", "Messi"]], ["Di Maria", "Dibu"])

def test_backtracking():
    _probar_algoritmo_con_archivos_de_ejemplo(hitting_set_backtracking, False)

def test_programacion_lineal():
    _probar_algoritmo_con_archivos_de_ejemplo(hitting_set_programacion_lineal, False)

def test_bilardo():
    _probar_algoritmo_con_archivos_de_ejemplo(hitting_set_aproximacion_bilardo, True)

def test_greedy():
    _probar_algoritmo_con_archivos_de_ejemplo(hitting_set_greedy, True)

def _probar_algoritmo_con_archivos_de_ejemplo(algoritmo, esAproximacion):
    ejemplos = [
        ("examples/5.txt", 2),
        ("examples/7.txt", 2),
        ("examples/10_pocos.txt", 3),
        ("examples/10_varios.txt", 6),
        ("examples/10_todos.txt", 10),
        ("examples/15.txt", 4),
        ("examples/20.txt", 5),
        ("examples/50.txt", 6),
        ("examples/75.txt", 8),
        # ("examples/100.txt", 9),
        # ("examples/200.txt", 9),
    ]
    for ruta_archivo, cantidad_minima_esperada in ejemplos:
        _probar_algoritmo(algoritmo, ruta_archivo, cantidad_minima_esperada, esAproximacion)

def _probar_algoritmo(algoritmo, ruta_archivo, cantidad_minima_esperada, esAproximacion):
    deseos = leer_archivo(ruta_archivo)
    cantidad_maxima_esperada = _contar_jugadores(deseos) if esAproximacion else cantidad_minima_esperada

    convocados = algoritmo(deseos)

    assert es_hitting_set(deseos, convocados)
    assert cantidad_minima_esperada <= len(convocados)
    assert cantidad_maxima_esperada >= len(convocados)

def _contar_jugadores(deseos):
    jugadores = set()
    for deseo in deseos:
        for jugador in deseo:
            jugadores.add(jugador)
    return len(jugadores)