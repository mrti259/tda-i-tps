ENTRENO = "Entreno"
DESCANSO = "Descanso"

def mejor_ganancia_greedy(dias, ganancia_por_dia, energia_por_dia):
    estrategia = []
    ganancia = 0
    dia_desde_descanso = 0
    
    for dia_entrenamiento in range(dias):
        ganancia_hoy = _ganancia_del_dia(dia_entrenamiento, dia_desde_descanso, ganancia_por_dia, energia_por_dia)
        ganancia_maniana = _ganancia_del_dia(dia_entrenamiento + 1, 0, ganancia_por_dia, energia_por_dia)

        if ganancia_maniana > ganancia_hoy:
            estrategia.append(DESCANSO)
            dia_desde_descanso = 0
            continue

        estrategia.append(ENTRENO)
        ganancia += ganancia_hoy
        dia_desde_descanso += 1
    
    return ganancia, estrategia

def _ganancia_del_dia(dia_entrenamiento, dia_desde_descanso, ganancia_por_dia, energia_por_dia):
    if dia_entrenamiento == len(ganancia_por_dia):
        return 0

    ganancia = ganancia_por_dia[dia_entrenamiento]
    energia = energia_por_dia[dia_desde_descanso]
    return min(ganancia, energia)

def mejor_ganancia(cant_dias, ganancia_por_dia, energia_por_dia):
    estrategia = []
    ganancia = 0  # Optimizamos por ganancia
    # Entrenamos ese dia o no son los branches
    ganancia = mejor_ganancia_recursiva(ganancia_por_dia, energia_por_dia, 0, 0)
    #ganancia = mejor_ganancia_dinamica(ganancia_por_dia, energia_por_dia)

    
    return ganancia, estrategia

def mejor_ganancia_recursiva(ganancia_por_dia, energia_por_dia, dia_a_analizar, dias_desde_descanso):
    if dia_a_analizar == len(ganancia_por_dia):
        return 0
    
    ganancia_entrenando = (_ganancia_del_dia(dia_a_analizar, dias_desde_descanso, ganancia_por_dia, energia_por_dia) 
                           + mejor_ganancia_recursiva(ganancia_por_dia, energia_por_dia, dia_a_analizar + 1, dias_desde_descanso + 1))
    ganancia_descansando = mejor_ganancia_recursiva(ganancia_por_dia, energia_por_dia, dia_a_analizar + 1, 0)

    return max (ganancia_entrenando, ganancia_descansando)

def mejor_ganancia_dinamica(ganancia_por_dia, energia_por_dia):
    pass

    

    
