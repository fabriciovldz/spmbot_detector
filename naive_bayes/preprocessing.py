import csv
import os

# Función para convertir texto en palabras (tokenizar)
def tokenize(text):
    return text.lower().replace("¿", "").replace("?", "").replace(",", "").split()

# Función para cargar los datos desde un archivo CSV
def cargar_datos():
    ruta_archivo = os.path.join("data", "text.csv")
    datos = []

    with open(ruta_archivo, newline='', encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            mensaje = fila["mensaje"].strip()
            etiqueta = fila["etiqueta"].strip().lower()
            datos.append([mensaje, etiqueta])

    return datos