import pytest

from tp1.tiempo_optimo import tiempo_optimo
from tp1.manejo_archivos_analisis import leer_archivo_analisis

def test_1():
    tiempo, analisis_ordenados = tiempo_optimo([])
    assert tiempo == 0

def test_2():
    datos = [
        (1,0),
    ]
    tiempo, analisis_ordenados = tiempo_optimo(datos)
    assert tiempo == 1

def test_3():
    datos = [
        (1,1),
    ]
    tiempo, analisis_ordenados = tiempo_optimo(datos)
    assert tiempo == 2

def test_4():
    datos = [
        (1,1),
        (1,0),
    ]
    tiempo, analisis_ordenados = tiempo_optimo(datos)
    assert tiempo == 2

def test_5():
    datos = [
        (1,3),
        (1,1),
    ]
    tiempo, analisis_ordenados = tiempo_optimo(datos)
    assert tiempo == 4

def test_6():
    datos = [
        (1,1),
        (1,3),
    ]
    tiempo, analisis_ordenados = tiempo_optimo(datos)
    assert tiempo == 4

def test_archivos():
    ejemplos = [
        ("data_enunciado/3 elem.txt", 10),
        ("data_enunciado/10 elem.txt", 29),
        ("data_enunciado/100 elem.txt", 5223),
        ("data_enunciado/10000 elem.txt", 497886735),
    ]
    for path, optimo in ejemplos:
        datos = leer_archivo_analisis(path)
        tiempo, analisis_ordenados = tiempo_optimo(datos)
        assert tiempo == optimo