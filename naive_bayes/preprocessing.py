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
