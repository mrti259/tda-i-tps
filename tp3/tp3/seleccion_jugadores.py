from tp3.archivos import leer_archivo
import HittingSetBacktracking
from pulp import LpMinimize, LpProblem, LpVariable, lpSum

def resolver_por_backtracking(archivo):
    deseos = leer_archivo(archivo)[1]
    selector = HittingSetBacktracking(deseos)
    return selector.buscar_solucion(deseos)

def resolver_por_programacion_lineal(archivo):
    deseos = leer_archivo(archivo)[1]
    return hitting_set_programacion_lineal(deseos)

def hitting_set_programacion_lineal(deseos):
    jugadores = set.union(*deseos)
    x = LpVariable.dicts('x', jugadores, cat='Binary')
    
    hitting_set = LpProblem("HittingSet", LpMinimize)
    hitting_set += lpSum(x[jugador] for jugador in jugadores)
    for deseo in deseos:
        hitting_set += lpSum(x[jugador] for jugador in deseo) >= 1

    hitting_set.solve()
    convocados = [jugador for jugador in jugadores if x[jugador].value() == 1]
    return convocados

def resolver_por_aproximacion_bilardo(archivo):
    deseos = leer_archivo(archivo)[1]
    return hitting_set_programacion_lineal(deseos)

def hitting_set_aproximacion_bilardo(deseos):
    b = max(len(deseo) for deseo in deseos)
    jugadores = set.union(*deseos)
    x = LpVariable.dict("x", jugadores, lowBound=0, upBound=1, cat='Continuous')
    
    hitting_set_aproximado = LpProblem(name="HittingSetAproximado", sense=LpMinimize)
    hitting_set_aproximado += lpSum(x[jugador] for jugador in jugadores)
    for deseo in deseos:
        hitting_set_aproximado += lpSum(x[jugador] for jugador in deseo) >= 1
        
    hitting_set_aproximado.solve()
    convocados = [jugador for jugador in jugadores if x[jugador].value() >= 1/b]
    return convocados

def resolver_greedy(archivo):
    deseos = leer_archivo(archivo)[1]
    return hitting_set_greedy(deseos)

def hitting_set_greedy(deseos_prensa):
    convocados = []

    while len(deseos_prensa) > 0:
        cant_jugadores = {}
        max = None
        
        for deseo in deseos_prensa:
            for jugador in deseo:
                cant_jugadores[jugador] = cant_jugadores.get(jugador, 0) + 1
                if not max or cant_jugadores[jugador] > cant_jugadores[max]:
                    max = jugador
                    
        convocados.append(max)
        deseos_prensa = _deseos_restantes(deseos_prensa, convocados)
    return convocados

def _deseos_restantes(deseos_prensa, convocados):
    deseos_restantes = []

    for deseo in deseos_prensa:
        cumplido = any(filter(lambda jugador: jugador in deseo, convocados))
        
        if not cumplido:
            deseos_restantes.append(deseo)
    
    return deseos_restantes