import pytest

# alumno_mas_bajo
from alumno_mas_bajo.solucion import validar_mas_bajo

# tests
from .utils import *

def test_1_validar_mas_bajo_sin_alumnos():
    with pytest.raises(ValueError):
        validar_mas_bajo([], 0)

def test_2_validar_mas_bajo_con_alumno_en_0():
    alumnos = [alice]
    assert validar_mas_bajo(alumnos, 0)

def test_3_validar_mas_bajo_con_alumno_distinto_a_0():
    alumnos = [alice]
    assert not validar_mas_bajo(alumnos, 1)

def test_4_validar_mas_bajo_con_dos_alumnos_decreciente_en_1():
    alumnos = [alice, bob]
    assert not validar_mas_bajo(alumnos, 0)

def test_5_validar_mas_bajo_con_dos_alumnos_decreciente_distinto_a_1():
    alumnos = [alice, bob]
    assert validar_mas_bajo(alumnos, 1)

def test_6_validar_mas_bajo_con_tres_alumnos_decreciente_en_2():
    alumnos = [alice, bob, carl]
    assert validar_mas_bajo(alumnos, 2)

def test_7_validar_mas_bajo_con_tres_alumnos_decreciente_distinto_a_2():
    alumnos = [alice, bob, carl]
    assert not validar_mas_bajo(alumnos, 1)

def test_8_validar_mas_bajo_con_cuatro_alumnos_decreciente_en_3():
    alumnos = [alice, bob, carl, daisy]
    assert validar_mas_bajo(alumnos, 3)

def test_9_validar_mas_bajo_con_cuatro_alumnos_decreciente_distinto_a_3():
    alumnos = [alice, bob, carl, daisy]
    assert not validar_mas_bajo(alumnos, 2)

def test_10_validar_mas_bajo_con_alumnos_decreciente_creciente_en_2():
    alumnos = [alice, bob, carl, emily, frank]
    assert validar_mas_bajo(alumnos, 2)

def test_11_validar_mas_bajo_con_alumnos_creciente_en_0():
    alumnos = [daisy, carl, bob, alice ]
    assert validar_mas_bajo(alumnos, 0)