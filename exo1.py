# Exercice 1
#Écrire, avec des comparaisons, un algorithme qui affiche l’état de l’eau (glace, liquide, vapeur) en fonction de sa température.

while True:
    temperature = input("la température de l'eau: ")
    if not temperature:
        break
    temperature = int(temperature)
    if temperature <= 0:
        print("\nC'est de la Glace")
    elif 0< temperature < 100:
        print("\nC'est du Liquide ") 
    else:
        print("\nC'est de la Vapeur")