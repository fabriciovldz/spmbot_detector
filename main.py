from naive_bayes.training import entrenar_naive_bayes
from naive_bayes.sorter import clasificar
from naive_bayes.preprocessing import cargar_datos

# Cargar dataset
textos = cargar_datos()

# Entrenar modelo
probs_clase, probs_palabra_dado_clase, vocabulario = entrenar_naive_bayes(textos)

# Clasificar nuevo texto
nuevo_texto = "Ofertas de relojes y perfumes"
resultado = clasificar(nuevo_texto, probs_clase, probs_palabra_dado_clase, vocabulario)

print(f"Resultado: {resultado}")