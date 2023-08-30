import sys
# Para el caso de querer implementar un DFS, 
# para que no hayan problemas en la prueba de volumen
sys.setrecursionlimit(10000)

def es_bipartito(grafo):
    s = set()
    t = set()

    for vertice in grafo:
        if not _recorrer(vertice, s, t, grafo):
            return False

    return True

def _recorrer(vertice, mismo_grupo, otro_grupo, grafo) -> bool:
    if vertice in mismo_grupo or vertice in otro_grupo:
        return True

    mismo_grupo.add(vertice)

    for adyacente in grafo.adyacentes(vertice):
        if adyacente in mismo_grupo:
            return False

        if not _recorrer(adyacente, otro_grupo, mismo_grupo, grafo):
            return False
    
    return True
