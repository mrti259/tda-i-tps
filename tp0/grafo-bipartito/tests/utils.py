class Grafo:
    def __init__(self, vertices: dict = {}):
        self._vertices = vertices

    def hay_arista(self, origen, destino) -> bool:
        raise NotImplementedError()
    
    def adyacentes(self, vertice) -> list[str]:
        return [*self._vertices.get(vertice, [])]
    
    def vertices(self) -> list[str]:
        raise NotImplementedError()
    
    def __iter__(self):
        return iter(self._vertices.keys())
    
    @classmethod
    def con_aristas(cls, aristas):
        vertices = {}
        for x,y in aristas:
            _agregar_arista(vertices, x, y)
            _agregar_arista(vertices, y, x)
        return cls(vertices)

def _agregar_arista(vertices, vertice, adyacente):
    adyacentes = vertices.get(vertice, set())
    adyacentes.add(adyacente)
    vertices[vertice] = adyacentes