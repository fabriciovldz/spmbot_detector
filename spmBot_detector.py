import os

estructura = {
    "clasificador_spam": {
        "data": {
            "textos.csv": ""  # Puedes llenarlo después si quieres usar CSV
        },
        "naive_bayes": {
            "__init__.py": "",
            "preprocesamiento.py": '''
def tokenize(text):
    return text.lower().replace("¿", "").replace("?", "").replace(",", "").split()

def cargar_datos():
    return [
        ["Nvidia GEFORCE GTX a buen precio", "spam"],
        ["Quedamos mañana lunes para ir al teatro", "nospam"],
        ["Réplicas de relojes y perfumes a precios de risa", "spam"],
        ["Disponga de sus relojes y demás productos en 24 horas", "spam"],
        ["¿Por qué la Inteligencia Artificial se considera un campo en desarrollo?", "nospam"],
    ]
''',
            "entrenamiento.py": '''
from collections import defaultdict
from .preprocesamiento import tokenize

def entrenar_naive_bayes(textos):
    palabras_por_clase = defaultdict(list)
    conteo_clases = defaultdict(int)

    for texto, etiqueta in textos:
        palabras = tokenize(texto)
        palabras_por_clase[etiqueta].extend(palabras)
        conteo_clases[etiqueta] += 1

    vocabulario = set(word for words in palabras_por_clase.values() for word in words)
    total_docs = sum(conteo_clases.values())

    probs_clase = {clase: conteo / total_docs for clase, conteo in conteo_clases.items()}
    
    probs_palabra_dado_clase = {}
    for clase, palabras in palabras_por_clase.items():
        total_palabras = len(palabras)
        frecuencia = defaultdict(int)
        for palabra in palabras:
            frecuencia[palabra] += 1
        probs_palabra_dado_clase[clase] = {
            palabra: (frecuencia[palabra] + 1) / (total_palabras + len(vocabulario))
            for palabra in vocabulario
        }

    return probs_clase, probs_palabra_dado_clase, vocabulario
'''
,
            "clasificador.py": '''
import math
from .preprocesamiento import tokenize

def clasificar(texto, probs_clase, probs_palabra_dado_clase, vocabulario):
    palabras = tokenize(texto)
    puntajes = {}

    for clase in probs_clase:
        log_prob = math.log(probs_clase[clase])
        for palabra in palabras:
            if palabra in vocabulario:
                log_prob += math.log(
                    probs_palabra_dado_clase[clase].get(palabra, 1 / (len(vocabulario) + 1))
                )
        puntajes[clase] = log_prob

    return max(puntajes, key=puntajes.get)
'''
        },
        "tests": {
            "test_modelo.py": "# Aquí puedes agregar tus pruebas unitarias"
        },
        "main.py": '''
from naive_bayes.entrenamiento import entrenar_naive_bayes
from naive_bayes.clasificador import clasificar
from naive_bayes.preprocesamiento import cargar_datos

# Cargar dataset
textos = cargar_datos()

# Entrenar modelo
probs_clase, probs_palabra_dado_clase, vocabulario = entrenar_naive_bayes(textos)

# Clasificar nuevo texto
nuevo_texto = "Ofertas de relojes y perfumes"
resultado = clasificar(nuevo_texto, probs_clase, probs_palabra_dado_clase, vocabulario)

print(f"Texto: '{nuevo_texto}'")
print(f"Clasificado como: {resultado}")
'''
    }
}

def crear_estructura(base_path, estructura):
    for nombre, contenido in estructura.items():
        ruta = os.path.join(base_path, nombre)
        if isinstance(contenido, dict):
            os.makedirs(ruta, exist_ok=True)
            crear_estructura(ruta, contenido)
        else:
            with open(ruta, "w", encoding="utf-8") as f:
                f.write(contenido.strip())

# Ejecutar
crear_estructura(".", estructura)
print("✅ Estructura del proyecto creada correctamente.")
