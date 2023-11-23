class HittingSetBacktracking():
    def __init__(self, deseos_prensa):
        self._solucion = None
        self._deseos_prensa = deseos_prensa
    
    def buscar_solucion(self):
        self._buscar_solucion(self._deseos_prensa, [], [])
        return self._solucion

    def _buscar_solucion(self, deseos_prensa, convocados, descartados):
        if self._solucion and len(self._solucion) <= len(convocados):
            return
            
        deseos_prensa = _deseos_restantes(deseos_prensa, convocados)
        
        if len(deseos_prensa) == 0:
            self._marcar_mejor_solucion(convocados)
            return
    
        jugador = _jugador_siguiente(deseos_prensa, descartados)
    
        if jugador == None:
            return
    
        if not _algun_deseo_se_puede_cumplir(deseos_prensa, descartados):
            return
                
        self._buscar_solucion(deseos_prensa, convocados, [*descartados, jugador])
        self._buscar_solucion(deseos_prensa, [*convocados, jugador], descartados)


    def _marcar_mejor_solucion(self, nueva_solucion):
        if not self._solucion or len(nueva_solucion) < len(self._solucion):
            self._solucion = nueva_solucion
            
        return self._solucion

def _deseos_restantes(deseos_prensa, convocados):
    deseos_restantes = []

    for deseo in deseos_prensa:
        cumplido = any(filter(lambda jugador: jugador in deseo, convocados))
        
        if not cumplido:
            deseos_restantes.append(deseo)
    
    return deseos_restantes

def _jugador_siguiente(deseos_prensa, descartados):
    for deseo in deseos_prensa:
        for jugador in deseo:
            if jugador in descartados:
                continue
            return jugador
    return None
    
def _algun_deseo_se_puede_cumplir(deseos_prensa, descartados):
    for deseo in deseos_prensa:
        if any(filter(lambda jugador: not jugador in descartados, deseo)):
            continue
        return False
    return True

def es_hitting_set(deseos_prensa, convocados):
    return not any(_deseos_restantes(deseos_prensa, convocados))