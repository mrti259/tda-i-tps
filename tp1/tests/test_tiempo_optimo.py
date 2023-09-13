import pytest

from tp1.tiempo_optimo import tiempo_optimo
from tp1.leer_archivo import leer_archivo

def test_1():
    assert tiempo_optimo([]) == 0

def test_2():
    datos = [
        (1,0),
    ]
    assert tiempo_optimo(datos) == 1

def test_3():
    datos = [
        (1,1),
    ]
    assert tiempo_optimo(datos) == 2

def test_4():
    datos = [
        (1,1),
        (1,0),
    ]
    assert tiempo_optimo(datos) == 2

def test_5():
    datos = [
        (1,3),
        (1,1),
    ]
    assert tiempo_optimo(datos) == 4

def test_6():
    datos = [
        (1,1),
        (1,3),
    ]
    assert tiempo_optimo(datos) == 4

def test_archivos():
    ejemplos = [
        ("data/3 elem.txt", 10),
        ("data/10 elem.txt", 29),
        ("data/100 elem.txt", 5223),
        ("data/10000 elem.txt", 497886735),
    ]
    for path, optimo in ejemplos:
        datos = leer_archivo(path)
        assert tiempo_optimo(datos) == optimo