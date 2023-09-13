import pytest

from tp1.leer_archivo import leer_archivo

def test_1():
    datos = leer_archivo("data_enunciado/3 elem.txt")
    assert len(datos) == 3

def test_2():
    datos = leer_archivo("data_enunciado/10 elem.txt")
    assert len(datos) == 10