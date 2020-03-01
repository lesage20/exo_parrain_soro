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
    


    
        
        
            
    
    
    



