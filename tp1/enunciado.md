# Trabajo Práctico 1: Algoritmos Greedy

El presente trabajo busca evaluar el desarrollo y análisis de un algoritmo Greedy. 
La fecha de entrega del mismo es el {{fecha}}.

## Introducción

Tenemos que ayudar a Scaloni a analizar los próximos $n$ rivales de la selección
campeona del mundo. Como técnico perfeccionista, quiere analizar videos de 
cada uno de los rivales. Recibió un compilado por cada rival, y necesita hacer un
análisis muy detallado, lo cual le implica tomar apuntes, analizar tácticas, ver
cuándo hay que hacerle un masaje a Messi, etc... Para que el análisis sea 
detallado, cada compilado no lo revisa únicamente él, sino también un ayudante. 

El análisis del rival $i$ le toma $s_i$ de tiempo a Scaloni, y luego $a_i$ al 
ayudante (independientemente de cuál ayudante lo vea). Lo bueno, es que
después de los grandes logros obtenidos, Scaloni cuenta con $n$ ayudantes (es
decir, la misma cantidad que rivales), que pueden ver los videos completamente 
en paralelo. Siempre los ayudantes podrán ver los videos **después** que Scaloni haya
terminado de verlo y analizarlo como corresponde (esto no lo delega). Cuando
llega la hora que un ayudante lo vea, puede ser cualquiera, pero sólo uno lo verá
(no hay ganancia en que dos lo vean). 

El DT necesita que los rivales estén todos con sus correspondientes análisis lo antes
posible, y por eso te pide que lo ayudes. Dice que confía en vos. Sabe que no lo 
vas a dejar tirado. 


## Consigna

1. Hacer un análisis del problema, y proponer un algoritmo greedy que obtenga **la solución óptima** al problema planteado: Dado los valores de $n$, los $s_i$ y $a_i$, determinar un orden en el que
Scaloni debe ver los videos tal que todos los análisis estén listos lo antes posible (es decir, en el mínimo tiempo necesario). Explicar detalladamente por qué el algoritmo planteado obtiene siempre la solución óptima. 
2. Francia. 
3. Escribir el algoritmo planteado. Describir y justificar la complejidad de dicho algoritmo. Analizar si (y cómo) afecta la variabilidad de los valores de $a_i$ y $s_i$ a los tiempos y optimalidad del algoritmo planteado. 
4. Realizar ejemplos de ejecución para encontrar soluciones y corroborar lo encontrado. Adicionalmente, el curso proveerá con algunos casos particulares que deben cumplirse su optimalidad también. 
5. De las pruebas anteriores, hacer también mediciones de tiempos para corroborar la complejidad teórica indicada. Realizar gráficos correspondientes. 
6. Agregar cualquier conclusión que parezca relevante.  

## Entrega

Completar el [formulario de entrega]({{site.data.cuatrimestre.entrega_tps}}) con los integrantes y el link al repositorio donde se encuentre el código fuente, y donde debe encontrarse el informe en formato PDF.
Debe ser claro cómo ejecutar el programa pasando por parámetro un set de datos como
los que se dan de ejemplo. Esto puede ser dentro del `README.md` del repositorio,
u otra que les parezca clara. 

El informe debe ser:
* Autocontenido: es decir, no debe ser necesario ponernos a buscar
el código por diferentes lugares.
* Tener todo el análisis correspondiente. 
* Ser realizado en un formato profesional. Para esto, les brindamos [un template]({{site.data.sitios.template_latex}}) en $\LaTeX$
para que puedan utilizar (también se encuentra en la home de la página del curso). 
No es necesario que lo sigan al pie de la letra, es simplemente un
ejemplo que tiene varias cosas que pueden llegar a utilizar de $\LaTeX$. Si ya conocen $\LaTeX$
no es necesario que lo utilicen, o mismo si utilizan algún otro formato (e.g. Markdown con
Pandoc), pero recomendamos su revisión para que vean cosas que no deben de faltar. Por supuesto,
pueden trabajar localmente como usar Overleaf o cualquier otra herramienta. El objetivo
de darles el template no es la de limitar la creatividad, sino de asegurarnos que se cumplan
lineamientos básicos sobre lo que se espera de una entrega de un informe en la facultad.
* En caso de ser necesarias reentregas, por favor agregar las modificaciónes en un Anexo al final del informe. No modificar lo hecho anteriormente.
La excepción a esto sería si hay que rehacer una enorme mayoría de lo escrito. 

La nota del trabajo práctico tendrá en cuenta tanto la presentación y calidad de lo presentado, 
como también el desarrollo del trabajo. No será lo mismo un trabajo realizado con lo mínimo
indispensable, que uno bien presentado, analizado, y probado con diferentes volúmenes, set de 
datos, o estrategias de generación de sets, en el caso que corresponda. 
