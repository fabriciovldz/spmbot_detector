from collections import defaultdict
from .preprocessing import tokenize

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
