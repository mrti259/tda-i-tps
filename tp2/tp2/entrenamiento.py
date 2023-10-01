ENTRENO = "Entreno"
DESCANSO = "Descanso"

def mejor_ganancia(dias, ganancia_por_dia, energia_por_dia):
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