def leer_archivo(ruta_entrada_archivo):
    """
    Los archivos tienen 1 conjunto (pedido de la prensa) por línea, separdos por ", ".
    """
    with open(ruta_entrada_archivo, 'r') as archivo:
        lineas = archivo.readlines()
    
    jugadores = set()
    deseos_prensa = []

    for linea in lineas:
        conjunto = [jugador.strip() for jugador in linea.split(',')]
        deseos_prensa.append(conjunto)
        jugadores.update(conjunto)

    return list(jugadores), deseos_prensa
