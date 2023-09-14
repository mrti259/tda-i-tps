from crear_archivo_de_analisis import crear_archivo_de_analisis
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python crear_archivos_de_analisis.py <cant_contricantes_primer_archivo> <cant_archivos> <incremento_contricantes_por_archivo>")
        sys.exit(1)

    cantidad_contricantes = int(sys.argv[1])
    cant_archivos = int(sys.argv[2])
    incremento_contricantes_por_archivo = int(sys.argv[3])

    for _ in range(cant_archivos):
        crear_archivo_de_analisis(f"tests/data/{cantidad_contricantes} elementos.txt", cantidad_contricantes)
        print(f"Se creo el archivo {cantidad_contricantes} elementos.txt.")
        cantidad_contricantes += incremento_contricantes_por_archivo

    