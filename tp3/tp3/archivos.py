import os

def leer_archivo(ruta_entrada_archivo):
    """
    Los archivos tienen 1 conjunto (pedido de la prensa) por línea, separados por ",".
    """
    with open(ruta_entrada_archivo, 'r') as archivo:
        lineas = archivo.readlines()
    
    deseos_prensa = []

    for linea in lineas:
        conjunto = [jugador.strip() for jugador in linea.split(',')]
        deseos_prensa.append(conjunto)

    return deseos_prensa

def guardar_convocados(convocados, ruta_salida):
    base_path = os.path.dirname(ruta_salida)
    if base_path:
        os.makedirs(base_path, exist_ok=True)
    with open(ruta_salida, "w") as archivo:
        archivo.write(f"{', '.join(convocados)}")
            
