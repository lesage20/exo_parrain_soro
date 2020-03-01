# Exercice 2
#Écrire le même algorithme, mais en utilisant deux variables booléennes pour vérifier l’état de l’eau, sans comparaisons dans les SI.

while True:
    temperature = input("température de l'eau: ")
    if not temperature:
        break
    temperature = int(temperature)
    a = (temperature <= 0)
    b = (0 < temperature < 100)
    msg = "c'est de la Glace !" if a else "c'est du Liquide " if b else "Oups de la Vapeur"
    print("\n", msg)