# TP3

## Dependencias

Para ejecutar el código es necesario tener Python instalado.
Además, para levantar un entorno virtual e instalar las dependencias, es recomendado instalar Poetry.

## Comandos

- Instalar dependencias: `poetry install` o `make install`
- Iniciar Jupyter Notebook: `poetry run jupyter notebook` o `make notebook`
- Ejecutar tests: `poetry run pytest` o `make test`
- Ejecutar programa con un archivo: `poetry run python tp3/selector.py <path/de/archivo_entrada.txt> <path/de/archivo_salida.txt> <metodo>` o `make run entrada=<path/de/archivo_entrada.txt> salida=<path/de/archivo_salida.txt> metodo=<metodo>`

## Formato de archivo

- Datos de entrada: los archivos tienen 1 conjunto (pedido de la prensa) por línea, separados por `","`.
- Datos de salida: los archivos tienen los jugadores seleccionados por el algoritmo, separados por `","`.

## Notebooks

- Comparación de tiempos de ejecución: `notebooks/Algoritmos.ipynb`
- Generador de sets de datos: `notebooks/Generador de archivos.ipynb`

## Reporte

En la raiz del directorio `report` se encuentra el informe en formato `.pdf` y luego dentro de `source` se encuentra la fuente del informe (archivos tex e imagenes).

## Autorxs

- Borja Garibotti
- Mauro Rizzi
- Julieta Taras
