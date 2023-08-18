import pytest

# grafo_bipartito
from grafo_bipartito.solucion import es_bipartito

# tests
from .utils import *

def test_1_iterar_grafo():
    grafo = Grafo()
    for v in grafo:
        pass