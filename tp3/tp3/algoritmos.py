from pulp import LpMinimize, LpProblem, LpVariable, lpSum

"""
Validación
"""

def es_hitting_set(deseos_prensa, convocados):
    """
    Una solución es válida si los jugadores convocados logran satisfacer todos los deseos de la prensa.
    """
    return not any(_deseos_pendientes(deseos_prensa, convocados))

def _deseos_pendientes(deseos_prensa, convocados):
    """
    Devuelve una lista con los deseos que faltan satisfacer.
    """
    deseos_restantes = []

    for deseo in deseos_prensa:
        cumplido = any(filter(lambda jugador: jugador in deseo, convocados))
        
        if not cumplido:
            deseos_restantes.append(deseo)
    
    return deseos_restantes

"""
Backtracking
"""

def hitting_set_backtracking(deseos):
    return HittingSetBacktracking(deseos).buscar_solucion()

class HittingSetBacktracking():
    def __init__(self, deseos_prensa):
        self._solucion = None
        self._deseos_prensa = deseos_prensa
    
    def buscar_solucion(self):
        """
        Busca la solución óptima por backtracking y la devuelve.
        """
        self._buscar_solucion(self._deseos_prensa, [], [])
        return list(self._solucion)

    def _buscar_solucion(self, deseos_pendientes, convocados, descartados):
        """
        Busca la solución óptima explorando primero las soluciones con la máxima cantidad de jugadores descartados.
        Una vez que se encuentra una solución se guarda en el estado interno de manera que en el backtracking se
        puedan descartar rápidamente los llamados que exploran soluciones más grandes.
        """
        if not self._puede_ser_solucion_optima(convocados):
            return
            
        deseos_pendientes = _deseos_pendientes(deseos_pendientes, convocados)
        
        if not any(deseos_pendientes):
            self._marcar_mejor_solucion(convocados)
            return
    
        jugador = _jugador_siguiente(deseos_pendientes, descartados)
    
        if jugador == None:
            return
    
        if not _todos_los_deseos_se_pueden_cumplir(deseos_pendientes, descartados):
            return
                
        self._buscar_solucion(deseos_pendientes, convocados, [*descartados, jugador])
        self._buscar_solucion(deseos_pendientes, [*convocados, jugador], descartados)


    def _marcar_mejor_solucion(self, nueva_solucion):
        """
        nueva_solucion es una solución válida. Si es óptima se guarda en el estado interno.
        """
        if self._puede_ser_solucion_optima(nueva_solucion):
            self._solucion = nueva_solucion
        
    def _puede_ser_solucion_optima(self, convocados):
        """
        Devuelve True si convocados puede ser una solución óptima, sin comprobar su validez.
        """
        return not self._solucion or len(convocados) < len(self._solucion)


def _jugador_siguiente(deseos_pendientes, descartados):
    """
    Devuelve el primer jugador que encuentra que es deseado por la prensa y no fue descartado en la solución explorada.
    """
    for deseo in deseos_pendientes:
        for jugador in deseo:
            if jugador in descartados:
                continue
            return jugador
    return None
    
def _todos_los_deseos_se_pueden_cumplir(deseos_prensa, descartados):
    """
    Devuelve False si algún deseo no se puede satisfacer porque todos los jugadores fueron descartados. 
    """
    for deseo in deseos_prensa:
        if any(filter(lambda jugador: not jugador in descartados, deseo)):
            continue
        return False
    return True

"""
Programación lineal
"""

def hitting_set_programacion_lineal(deseos):
    deseos = [set(jugador) for jugador in deseos]

    jugadores = set.union(*deseos)
    x = LpVariable.dicts('x', jugadores, cat='Binary')
    
    hitting_set = LpProblem("HittingSet", LpMinimize)
    hitting_set += lpSum(x[jugador] for jugador in jugadores)
    for deseo in deseos:
        hitting_set += lpSum(x[jugador] for jugador in deseo) >= 1

    hitting_set.solve()
    convocados = [jugador for jugador in jugadores if x[jugador].value() == 1]
    return convocados

"""
Aproximación Bilardo
"""

def hitting_set_aproximacion_bilardo(deseos):
    deseos = [set(jugador) for jugador in deseos]
    
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

"""
Aproximación Greedy
"""

def hitting_set_greedy(deseos_prensa):
    """
    Encuentra una solución al problema eligiendo a aquellos jugadores que son más deseados y descartando
    en cada iteración los deseos que se satisfacen.
    """
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
        deseos_prensa = _deseos_pendientes(deseos_prensa, convocados)
    return convocados