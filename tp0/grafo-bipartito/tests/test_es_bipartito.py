import pytest

# grafo_bipartito
from grafo_bipartito.solucion import es_bipartito

# tests
from .utils import *

def test_1_iterar_grafo():
    grafo = Grafo()
    for v in grafo:
        pass

def test_2_grafo_bipartito_sin_aristas():
    grafo = Grafo()
    assert es_bipartito(grafo)

def test_3_grafo_no_bipartito_con_aristas():
    aristas = [
        "ab",
        "ac",
        "bc"
    ]
    grafo = Grafo.con_aristas(aristas)
    assert not es_bipartito(grafo)

def test_4_grafo_bipartito_con_aristas():
    aristas = [
        "ab",
        "ac",
    ]
    grafo = Grafo.con_aristas(aristas)
    assert es_bipartito(grafo)