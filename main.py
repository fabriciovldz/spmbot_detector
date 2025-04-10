from naive_bayes.training import entrenar_naive_bayes
from naive_bayes.sorter import clasificar
from naive_bayes.preprocessing import cargar_datos

# Entrenar modelo
textos = cargar_datos()
probs_clase, probs_palabra_dado_clase, vocabulario = entrenar_naive_bayes(textos)

# Modo interactivo
print("=== Clasificador de SPAM ===")
print("Escribe un mensaje y te diré si es SPAM o NO SPAM.")
print("Escribe 'salir' para terminar.\n")

while True:
    nuevo_texto = input("Tu mensaje: ").strip()
    if nuevo_texto.lower() == "salir":
        print("¡Hasta luego!")
        break

    resultado = clasificar(nuevo_texto, probs_clase, probs_palabra_dado_clase, vocabulario)
    print(f"➡️  Resultado: {resultado.upper()}\n")