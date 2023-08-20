def validar_mas_bajo(alumnos, indice):
    cantidad = len(alumnos)
    if cantidad == 0:
        raise ValueError("No hay alumnos")
    
    if cantidad < indice:
        return False

    if cantidad == 1:
        return indice == 0
    
    alumno = alumnos[indice]

    if indice != 0:
        anterior = alumnos[indice - 1]
        if not _es_mas_bajo(alumno, anterior):
            return False
    
    if indice != (cantidad - 1):
        siguiente = alumnos[indice + 1]
        if _es_mas_bajo(siguiente, alumno):
            return False
    
    return True

def indice_mas_bajo(alumnos):
    cantidad = len(alumnos)
    if cantidad == 0:
        raise ValueError("No hay alumnos")

    return _indice_mas_bajo_rec(alumnos, 0, cantidad)

def _indice_mas_bajo_rec(alumnos, inicial, final):
    cantidad = len(alumnos[inicial:final])

    if cantidad == 1:
        return inicial

    mitad = inicial + (cantidad // 2)
    medio = alumnos[mitad]
    anterior = alumnos[mitad - 1]

    if _es_mas_bajo(anterior, medio):
        return _indice_mas_bajo_rec(alumnos, inicial, mitad)
    
    i_menor_der = _indice_mas_bajo_rec(alumnos, mitad, final)
    menor_der = alumnos[i_menor_der]

    if _es_mas_bajo(menor_der, anterior):
        return i_menor_der
    
    return _indice_mas_bajo_rec(alumnos, inicial, mitad)

def _es_mas_bajo(alumno, otro):
    return alumno.altura < otro.altura