import pytest
import os

from tp2.archivos import *

RUTA_EJEMPLOS = "examples"

def test_1_leer_archivo():
    ruta = os.path.join(RUTA_EJEMPLOS, "3.txt")
    ganancia_por_dia, energia_por_dia = leer_archivo(ruta)
    dias = 3
    assert len(ganancia_por_dia) == dias
    assert len(energia_por_dia) == dias

def test_2_leer_archivo():
    ruta = os.path.join(RUTA_EJEMPLOS, "10.txt")
    ganancia_por_dia, energia_por_dia = leer_archivo(ruta)
    dias = 10
    assert len(ganancia_por_dia) == dias
    assert len(energia_por_dia) == dias

def test_3_guardar_estrategia():
    salida = "/tmp/test_3_guardar_estrategia.txt"
    estrategia = [
        "asd",
        "fgh",
        "jkl",
    ]
    guardar_estrategia(estrategia, salida)