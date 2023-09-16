# TP1

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
- Ejecutar programa con un archivo: `poetry run python analizar.py <path/de/archivo_entrada.txt> <path/de/archivo_salida.txt>` o `make run file_in=<path/de/archivo_entrada.txt> file_out=<path/de/archivo_salida.txt>`

## Formato de archivo

El archivo a leer debe cumplir el siguiente formato:
- El contenido de la primera línea será ignorado. Se espera que indique a qué campos corresponden los datos.
- Las lineas siguientes deben tener un valor entero que indique el tiempo de Scaloni $s_i$ para un contrincante $i$, seguido por una coma (",") y por otro entero que indique el tiempo del ayudante $a_i$ para el mismo rival.

```
S_i,A_i
3,3
5,1
1,8
```

## Notebooks

- Observaciones al ordenar los tiempos de Scaloni de menor a mayor: `notebooks/tp1-S_i-menor_a_mayor.ipynb`
- Observaciones al ordenar los tiempos de los ayudantes de mayor a menor: `notebooks/tp1-A_i-mayor_a_menor.ipynb`
- Generación de archivos para pruebas de carga: `notebooks/Crear archivos de analisis.ipynb`
- Cálculos de tiempos de ejecución con gran volumen de datos: `notebooks/Calculo de tiempos.ipynb`

## Autorxs

- Borja Garibotti
- Mauro Rizzi
- Julieta Taras 