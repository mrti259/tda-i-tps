def tiempo_optimo(datos):
    tiempo_maximo = 0
    tiempo_inicial = 0

    datos = sorted(datos, key=lambda x: x[1], reverse=True)

    for (s_i, a_i) in datos:
        tiempo_actual = tiempo_inicial + s_i + a_i
        tiempo_inicial += s_i

        if tiempo_actual > tiempo_maximo:
            tiempo_maximo = tiempo_actual
    
    return tiempo_maximo