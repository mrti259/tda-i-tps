ENTRENO = "Entreno"
DESCANSO = "Descanso"

def _ganancia_del_dia(dia_entrenamiento, dia_desde_descanso, ganancia_por_dia, energia_por_dia):
    if dia_entrenamiento == len(ganancia_por_dia):
        return 0

    ganancia = ganancia_por_dia[dia_entrenamiento]
    energia = energia_por_dia[dia_desde_descanso]
    return min(ganancia, energia)

def mejor_ganancia(ganancia_por_dia, energia_por_dia):
    estrategia = []
    ganancia = mejor_ganancia_dinamico(ganancia_por_dia, energia_por_dia)
    return ganancia, estrategia

def mejor_ganancia_greedy(ganancia_por_dia, energia_por_dia):
    estrategia = []
    ganancia = 0
    dias_desde_ultimo_descanso = 0
    dias_de_entrenamiento = len(ganancia_por_dia)
    
    for dia_entrenamiento in range(dias_de_entrenamiento):
        ganancia_hoy_si_entreno = _ganancia_del_dia(dia_entrenamiento, dias_desde_ultimo_descanso, ganancia_por_dia, energia_por_dia)
        ganancia_maniana_si_descanso = _ganancia_del_dia(dia_entrenamiento + 1, 0, ganancia_por_dia, energia_por_dia)

        if ganancia_maniana_si_descanso > ganancia_hoy_si_entreno:
            estrategia.append(DESCANSO)
            dias_desde_ultimo_descanso = 0
            continue

        estrategia.append(ENTRENO)
        ganancia += ganancia_hoy_si_entreno
        dias_desde_ultimo_descanso += 1
    
    return ganancia, estrategia

def mejor_ganancia_recursivo(ganancia_por_dia, energia_por_dia, dia_a_analizar, dias_desde_descanso):
    if dia_a_analizar == len(ganancia_por_dia):
        return 0
    
    ganancia_entrenando_hoy = (_ganancia_del_dia(dia_a_analizar, dias_desde_descanso, ganancia_por_dia, energia_por_dia) 
                           + mejor_ganancia_recursivo(ganancia_por_dia, energia_por_dia, dia_a_analizar + 1, dias_desde_descanso + 1))
    ganancia_descansando_hoy = mejor_ganancia_recursivo(ganancia_por_dia, energia_por_dia, dia_a_analizar + 1, 0)

    return max(ganancia_entrenando_hoy, ganancia_descansando_hoy)

def mejor_ganancia_recursivo_con_memoria(ganancia_por_dia, energia_por_dia, dia_a_analizar, dias_desde_descanso, M):
    if dia_a_analizar == len(ganancia_por_dia):
        return 0
    
    ganancia_guardada = M[dia_a_analizar][dias_desde_descanso]

    if ganancia_guardada != None:
        return ganancia_guardada

    ganancia_entrenando_hoy = (_ganancia_del_dia(dia_a_analizar, dias_desde_descanso, ganancia_por_dia, energia_por_dia) 
                        + mejor_ganancia_recursivo_con_memoria(ganancia_por_dia, energia_por_dia, dia_a_analizar + 1, dias_desde_descanso + 1, M))
    ganancia_descansando_hoy = mejor_ganancia_recursivo_con_memoria(ganancia_por_dia, energia_por_dia, dia_a_analizar + 1, 0, M)

    ganancia_guardada = max(ganancia_entrenando_hoy, ganancia_descansando_hoy)

    M[dia_a_analizar][dias_desde_descanso] = ganancia_guardada
    
    return ganancia_guardada

def mejor_ganancia_dinamico(ganancia_por_dia, energia_por_dia):
    dias_de_entrenamiento = len(ganancia_por_dia)
    dias_desde_descanso = 0
    ganancia = 0

    M = []

    for dia_a_analizar in range(dias_de_entrenamiento):
        for dia_desde_descanso in range(dia_a_analizar):
            M[dia_a_analizar][dia_desde_descanso] = _ganancia_del_dia(dia_a_analizar, dia_desde_descanso, ganancia_por_dia, energia_por_dia)

        ganancia_entrenando_hoy = (M[dia_a_analizar][dias_desde_descanso] + M[dia_a_analizar + 1][dias_desde_descanso + 1])
        ganancia_descansando_hoy = M[dia_a_analizar + 1][0]

        if ganancia_descansando_hoy > ganancia_entrenando_hoy:
            dias_desde_descanso = 0
            continue

        ganancia += ganancia_entrenando_hoy
        dias_desde_descanso += 1
    
    return ganancia