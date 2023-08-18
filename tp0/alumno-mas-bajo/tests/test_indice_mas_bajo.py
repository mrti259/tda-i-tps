import pytest

# alumno_mas_bajo
from alumno_mas_bajo.solucion import indice_mas_bajo, validar_mas_bajo

# tests
from .utils import *

def test_1_indice_mas_bajo_sin_alumnos():
    with pytest.raises(ValueError):
        indice_mas_bajo([])

def test_2_indice_mas_bajo_con_alumno_es_0():
    alumnos = [alice]
    assert indice_mas_bajo(alumnos) == 0

def test_3_indice_mas_bajo_con_alumnos_decreciente_es_1():
    alumnos = [alice, bob]
    assert indice_mas_bajo(alumnos) == 1

def test_4_indice_mas_bajo_con_alumnos_creciente_es_0():
    alumnos = [bob, alice]
    assert indice_mas_bajo(alumnos) == 0

def test_5_indice_mas_bajo_con_alumnos_decreciente_creciente_es_3():
    alumnos = [alice, bob, carl, daisy, emily, frank]
    assert indice_mas_bajo(alumnos) == 3

def test_6_indice_mas_bajo_con_alumnos_decreciente_creciente_es_2():
    alumnos = [bob, carl, daisy, emily, frank]
    assert indice_mas_bajo(alumnos) == 2

def test_7_indice_mas_bajo_con_alumnos_decreciente_es_3():
    alumnos = [alice, bob, carl, daisy]
    assert indice_mas_bajo(alumnos) == 3

def test_8_carga():
    nombre = ""
    alumnos = [Alumno(nombre, altura) for altura in range(20, 100001)][::-1]
    alumnos += [Alumno(nombre, altura) for altura in range(21, 200000)]
    assert indice_mas_bajo(alumnos) == 99980