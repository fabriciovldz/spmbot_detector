import math
from .preprocessing import tokenize

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
