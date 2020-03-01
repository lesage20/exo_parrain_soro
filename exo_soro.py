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
    

# exo 4
def exo4():
    p = 0.9
    x = 2
    f = "p**x - (1/x)"
    e = "p**(x+1) - (1/(x+1))"
    while eval(e) > eval(f):
        x += 1
    print(eval(e),   eval(f),  x) 


# exo 5
def exo5():
    
    tarifs = ["bleu", "vert", "orange" ,"rouge"]
    tarif = ""
    age = int(input("Veuillez saisir votre age "))
    temps_permis = int(input("Depuis Combien d'années vous avez le permis? "))
    accident = int(input("Combien d'accident avez vous fait depuis l'obtention de votre permis ")) 
    assurance = False
    satisfait = int(input("Depuis Combien d'années vous etes clients chez nous? "))
    
    if age <= 25 and temps_permis <=2:
        if not accident :
            tarif = tarifs[-1]
            assurance = True
            
        else:
            assurance = False
        
    elif (age <= 25 and temps_permis > 2) or (age > 25 and temps_permis <= 2):
        if accident == 0:
            tarif = tarifs[-2]
            assurance = True
            
        elif accident == 1:
            tarif = tarifs[-1]
            assurance = True
            
            
        else:
            assurance = False
        
                    
    elif age > 25 and temps_permis > 2:
        if accident == 0:
            tarif = tarifs[1]
            assurance = True
            
        elif accident == 1:
            tarif= tarifs[-2]
            assurance == True
        elif accident == 2:
            tarif= tarifs[-1]
            assurance == True
        else:
            assurance = False
    if assurance == True:
        if satisfait > 5:
            tarif = tarifs[tarifs.index(tarif) -1]
        else:
            tarif = tarif
    print("votre tarif est : ", tarif)
    
exo5()
    


    
        
        
            
    
    
    



