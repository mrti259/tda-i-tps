import os

def leer_archivo(ruta_entrada):
    """
    El formato de los sets de datos es: 
    En la primera línea el valor de la cantidad de días a considerar (n)
    En las siguientes n líneas, las ganancias de dichos días (nuestros e_i).
    En las siguientes n líneas, la energía con la que se cuenta al día 1, 2, 3, ..., n de estar entrenando sin haber descansando previamente (nuestros s_i).
    """
    with open(ruta_entrada) as archivo:
        dias = int(archivo.readline())
        ganancia_por_dia = [int(archivo.readline()) for _ in range(dias)]
        energia_por_dia = [int(archivo.readline()) for _ in range(dias)]
        return ganancia_por_dia, energia_por_dia

def guardar_estrategia(estrategia, ruta_salida):
    base_path = os.path.dirname(ruta_salida)
    os.makedirs(base_path, exist_ok=True)
    with open(ruta_salida, "w") as archivo:
        for dia in estrategia:
            archivo.write(dia)
            archivo.write("\n")