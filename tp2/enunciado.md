# **Trabajo Práctico 2: Programación Dinámica**

El presente trabajo busca evaluar el desarrollo y análisis de un algoritmo de Programación Dinámica. La fecha de entrega del mismo es el 9/10.

## **Introducción**


Luego de haber analizado a todos los rivales gracias a tu ayuda, Scaloni definió un cronograma de entrenamiento. Tiene definido qué hacer para cada día de acá al mundial que viene, e incluso más. Para hacerlo más simple, para los próximos $`n`$ días. El entrenamiento del día $`i`$ demanda una cantidad de esfuerzo $`e_i`$, y podemos decir que la *ganancia* que nos da dicho entrenamiento es igual al esfuerzo. El entrenamiento que corresponde al día $`i`$ (así como su esfuerzo y ganancia) son inamovibles: el Chiqui Tapia alquiló las herramientas específicas para cada día, y la AFA está muy ocupada organizando el torneo de 230230 equipos del año que viene para andar moviendo cosas. Si la cantidad de energía que se tiene para un día i*i* es j<ei*j*<*ei*, entonces la ganancia que se obtiene en ese caso es justamente j*j*. (si se tiene más energía que ei*ei*, no es que se pueda usar más para tener más ganancia).

A su vez, los jugadores no son máquinas. La cantidad de energía que tienen disponible para cada día va disminuyendo a medida que pasan los entrenamientos. Suponiendo que los entrenamientos empiezan con los jugadores descansados, el primer día luego de dicho descanso los jugadores tienen energía s1*s*1. El segundo día luego del descanso tienen energía s2*s*2, etc… Para cada día hay una cantidad de energía, y podemos decir que s1≤s2≤...≤sn*s*1≤*s*2≤...≤*sn*. Scaloni puede decidir dejarlos descansar un día, haciendo que la energía “se renueve” (es decir, el próximo entrenamiento lo harían con energía s1*s*1 nuevamente, siguiendo con s2*s*2, etc…). Obviamente, si descansan, el entrenamiento de ese día no se hace (y no se consigue ninguna ganancia).

Scaloni no sabe bien cómo hacer para definir los días que deba entrenarse y los días que convenga descansar de tal forma de tener la mayor ganancia posible (y tener mayores probabilidades de ganar el mundial que viene), pero Menotti, exponente del juego bonito en Argentina, le recomendó usar Programación Dinámica para resolver este problema. Nos está pidiendo ayuda para poder resolver este problema.

## **Consigna**

1. Hacer un análisis del problema, plantear la ecuación de recurrencia correspondiente y proponer un algoritmo por programación dinámica que obtenga la solución óptima al problema planteado: Dada la secuencia de energía disponible desde el último descanso *s*1,*s*2,...,*sn*, y el esfuerzo/ganancia de cada día *ei*, determinar la máxima cantidad de ganancia que se obtener de los entrenamientos, considerando posibles descansos.
    
    s1,s2,...,sn
    
    ei
    
2. Escribir el algoritmo planteado. Describir y justificar la complejidad de dicho algoritmo. Analizar si (y cómo) afecta la variabilidad de los valores de los esfuerzos (disponibles y necesarios) a los tiempos y optimalidad del algoritmo planteado.
3. Realizar ejemplos de ejecución para encontrar soluciones y corroborar lo encontrado. Adicionalmente, el curso proveerá con algunos casos particulares que deben cumplirse su optimalidad también.
4. De las pruebas anteriores, hacer también mediciones de tiempos para corroborar la complejidad teórica indicada. Realizar gráficos correspondientes.
5. Agregar cualquier conclusión que parezca relevante.

## **Entrega**

Debe enviarse al corrector asignado, por mail o slack, el link al repositorio donde se encuentre el código fuente, y donde debe encontrarse el informe en formato PDF, que debe seguir los lineamientos establecidos en el TP1. Debe ser claro cómo ejecutar el programa pasando por parámetro un set de datos como los que se dan de ejemplo. Esto puede ser dentro del `README.md` del repositorio, u otra forma que les parezca clara.

La nota del trabajo práctico tendrá en cuenta tanto la presentación y calidad de lo presentado, como también el desarrollo del trabajo. No será lo mismo un trabajo realizado con lo mínimo indispensable, que uno bien presentado, analizado, y probado con diferentes volúmenes, set de datos, o estrategias de generación de sets, en el caso que corresponda.