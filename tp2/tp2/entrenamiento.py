from typing import Tuple, List

ENTRENO = 1
DESCANSO = 0

def mejor_ganancia(ganancia_por_dia, energia_por_dia) -> Tuple[int, List[int]]:
    return mejor_ganancia_iterativo(ganancia_por_dia, energia_por_dia)

def _ganancia_del_dia(dia_entrenamiento, dia_desde_descanso, ganancia_por_dia, energia_por_dia) -> int:
    if dia_entrenamiento == len(ganancia_por_dia):
        return 0

    ganancia = ganancia_por_dia[dia_entrenamiento]
    energia = energia_por_dia[dia_desde_descanso]
    return min(ganancia, energia)

"""
Algoritmo Greedy
"""

def mejor_ganancia_greedy(ganancia_por_dia, energia_por_dia) -> Tuple[int, List[int]]:
    plan = []
    ganancia = 0
    dias_desde_ultimo_descanso = 0
    dias_de_entrenamiento = len(ganancia_por_dia)
    
    for dia_entrenamiento in range(dias_de_entrenamiento):
        ganancia_hoy_si_entreno = _ganancia_del_dia(dia_entrenamiento, dias_desde_ultimo_descanso, ganancia_por_dia, energia_por_dia)
        ganancia_maniana_si_descanso = _ganancia_del_dia(dia_entrenamiento + 1, 0, ganancia_por_dia, energia_por_dia)

        if ganancia_maniana_si_descanso > ganancia_hoy_si_entreno:
            plan.append(DESCANSO)
            dias_desde_ultimo_descanso = 0
            continue

        plan.append(ENTRENO)
        ganancia += ganancia_hoy_si_entreno
        dias_desde_ultimo_descanso += 1
    
    return ganancia, plan

"""
Algoritmo recursivo
"""

def mejor_ganancia_recursivo(ganancia_por_dia, energia_por_dia) -> Tuple[int, List[int]]:
    plan = [] #TODO
    ganancia = _mejor_ganancia_recursivo(ganancia_por_dia, energia_por_dia, 0, 0)
    return ganancia, plan

def _mejor_ganancia_recursivo(ganancia_por_dia, energia_por_dia, dia_a_analizar, dias_desde_descanso) -> int:
    if dia_a_analizar == len(ganancia_por_dia):
        return 0
    
    ganancia_entrenando_hoy = (_ganancia_del_dia(dia_a_analizar, dias_desde_descanso, ganancia_por_dia, energia_por_dia) 
            + _mejor_ganancia_recursivo(ganancia_por_dia, energia_por_dia, dia_a_analizar + 1, dias_desde_descanso + 1))
    ganancia_descansando_hoy = _mejor_ganancia_recursivo(ganancia_por_dia, energia_por_dia, dia_a_analizar + 1, 0)

    return max(ganancia_entrenando_hoy, ganancia_descansando_hoy)

"""
Algoritmo recursivo con Memoización
"""

def mejor_ganancia_recursivo_con_memoria(ganancia_por_dia, energia_por_dia) -> Tuple[int, List[int]]:
    cant_dias = len(ganancia_por_dia)
    M = [[None for _ in range(cant_dias)] for _ in range(cant_dias)]
    ganancia = _mejor_ganancia_recursivo_con_memoria(ganancia_por_dia, energia_por_dia, 0, 0, M)
    plan = _reconstruir_plan_de_entrenamiento_desde_memo(M, ganancia_por_dia, energia_por_dia)
    return ganancia, plan

def _mejor_ganancia_recursivo_con_memoria(ganancia_por_dia, energia_por_dia, dia_a_analizar, dias_desde_descanso, M) -> int:
    if dia_a_analizar == len(ganancia_por_dia):
        return 0
    
    ganancia_guardada = M[dia_a_analizar][dias_desde_descanso]

    if ganancia_guardada != None:
        return ganancia_guardada

    ganancia_entrenando_hoy = (_ganancia_del_dia(dia_a_analizar, dias_desde_descanso, ganancia_por_dia, energia_por_dia) 
                        + _mejor_ganancia_recursivo_con_memoria(ganancia_por_dia, energia_por_dia, dia_a_analizar + 1, dias_desde_descanso + 1, M))
    ganancia_descansando_hoy = _mejor_ganancia_recursivo_con_memoria(ganancia_por_dia, energia_por_dia, dia_a_analizar + 1, 0, M)

    ganancia_guardada = max(ganancia_entrenando_hoy, ganancia_descansando_hoy)

    M[dia_a_analizar][dias_desde_descanso] = ganancia_guardada
    
    return ganancia_guardada

"""
Algoritmo iterativo con Memoización
"""

def mejor_ganancia_iterativo(ganancia_por_dia, energia_por_dia) -> Tuple[int, List[int]]:
    cant_dias = len(ganancia_por_dia)

    M = [[0 for _ in range(cant_dias+1)] for _ in range(cant_dias+1)]
    
    for dia_a_analizar in range(cant_dias):
        for dias_desde_descanso in range(dia_a_analizar + 1):
            M[dia_a_analizar][dias_desde_descanso] = _ganancia_del_dia(dia_a_analizar, dias_desde_descanso, ganancia_por_dia, energia_por_dia)
    
    for dia_a_analizar in range(cant_dias-1, -1, -1):
        for dias_desde_descanso in range(dia_a_analizar + 1):
            ganancia_si_descanso = M[dia_a_analizar+1][0]
            ganancia_si_entreno = M[dia_a_analizar][dias_desde_descanso] + M[dia_a_analizar+1][dias_desde_descanso+1]
            M[dia_a_analizar][dias_desde_descanso] = max(ganancia_si_descanso, ganancia_si_entreno)
    
    ganancia= M[0][0]
    plan = _reconstruir_plan_de_entrenamiento_desde_memo(M, ganancia_por_dia, energia_por_dia)
    return ganancia, plan
    
def _reconstruir_plan_de_entrenamiento_desde_memo(M, ganancia_por_dia, energia_por_dia) -> List[int]:
    cant_dias = len(ganancia_por_dia)
    plan = []

    dias_desde_descanso = 0
    for dia_a_analizar in range(cant_dias):
        # el ultimo día siempre entreno
        if dia_a_analizar == cant_dias - 1:
            plan.append(ENTRENO)
            dias_desde_descanso += 1
            continue

        ganancia_optima = M[dia_a_analizar][dias_desde_descanso]
        ganancia_del_dia = _ganancia_del_dia(dia_a_analizar, dias_desde_descanso, ganancia_por_dia, energia_por_dia)
        ganancia_si_entreno = M[dia_a_analizar+1][dias_desde_descanso+1]

        if ganancia_optima == ganancia_del_dia + ganancia_si_entreno:
            plan.append(ENTRENO)
            dias_desde_descanso += 1
            continue

        plan.append(DESCANSO)
        dias_desde_descanso = 0

    return plan