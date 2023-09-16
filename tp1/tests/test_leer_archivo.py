import pytest

from tp1.manejo_archivos_analisis import leer_archivo_analisis

def test_1():
    datos = leer_archivo_analisis("data_enunciado/3 elem.txt")
    assert len(datos) == 3

def test_2():
    datos = leer_archivo_analisis("data_enunciado/10 elem.txt")
    assert len(datos) == 10