# TP2

## Dependencias

Para ejecutar el código es necesario tener Python instalado.
Además, para levantar un entorno virtual e instalar las dependencias, es recomendado instalar Poetry.

``` sh
pip install poetry
```

## Comandos

- Instalar dependencias: `poetry install` o `make install`
- Iniciar Jupyter Notebook: `poetry run jupyter notebook` o `make notebook`
- Ejecutar tests: `poetry run pytest` o `make test`
- Ejecutar programa con un archivo: `poetry run python tp2/cli.py <path/de/archivo_entrada.txt> <path/de/archivo_salida.txt>` o `make run file_in=<path/de/archivo_entrada.txt> file_out=<path/de/archivo_salida.txt>`

## Formato de archivo

El formato de los sets de datos es: 
En la primera línea el valor de la cantidad de días a considerar (n)
En las siguientes n líneas, las ganancias de dichos días (nuestros e_i).
En las siguientes n líneas, la energía con la que se cuenta al día 1, 2, 3, ..., n de estar entrenando sin haber descansando previamente (nuestros s_i).

## Notebooks

TODO

## Reporte

En la raiz del directorio `report` se encuentra el informe en formato `.pdf` y luego dentro de `source` se encuentra la fuente del informe (archivos tex e imagenes).

## Autorxs

- Borja Garibotti
- Mauro Rizzi
- Julieta Taras 