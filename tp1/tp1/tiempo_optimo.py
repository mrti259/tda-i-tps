def tiempo_optimo(tiempos_analisis):
    tiempo_fin_maximo = 0
    tiempo_actual = 0

    tiempos_analisis = sorted(tiempos_analisis, key=lambda analisis: analisis[1], reverse=True)

    for (tiempo_scaloni, tiempo_ayudante) in tiempos_analisis:
        # Scaloni ve el video
        tiempo_actual += tiempo_scaloni

        # Cuando estaria terminado el analisis de este contricante
        tiempo_fin_analisis_actual = tiempo_actual + tiempo_ayudante

        # Si va a ser el ultimo en terminar de analizarse me lo guardo
        if tiempo_fin_analisis_actual > tiempo_fin_maximo:
            tiempo_fin_maximo = tiempo_fin_analisis_actual  

    return tiempo_fin_maximo