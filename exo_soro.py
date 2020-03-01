# # exo 1
# def exo1():
#     eau = ""
#     try:
#         x = input("Entrez la temperature de l'eau: ")
#         x = int(x) 
#         def affiche():
#             print(f"l'eau est a l'etat: {eau}")
#         if x <= 0:
#             eau = "solide"
#             affiche()
#         elif 0 < x < 100:
#             eau = "liquide" 
#             affiche()
#         elif x >= 100:
#             eau = "gazeux"
#             affiche()
#         elif type(x) == str :
#             print("OOOOPS VEUILLEZ ENTRER DES CHIFFRE SVP")
#     except ValueError:
#         print("Vous avez entrer de mauvaise données veuillez verifier la valeur doit etre un nombre")
            



# # exo2

# def exo2():
#     eau = ""
#     try:
#         i = input("Entrez la temperature de l'eau: ")
#         i=int(i)
#         x = i <= 0
#         y = [range(100)] 
#         def affiche():
#             print(f"l'eau est a l'etat: {eau}")
#         if bool(x):
#             eau = "solide"
            
#             affiche()
#         elif x is False and  i in range(100):
#                 eau = "liquide" 
                
#                 affiche()
#         elif x is False and not i in range(100) :
#                 eau = "gazeux"
#                 affiche()
        
#     except ValueError:
#         print("Vous avez entrer de mauvaise données veuillez verifier la valeur doit etre un nombre")



# exo 3
def exo3():
    n = 0
    liste = [n]
    a = input("entrez un nombre: ")
    a = int(a)
    while sum(liste) < int(a) + 1 :
        n = n + 1
        liste.append(n)
    print(f"Le plut petit entier est : {n} et Hn = ", sum(liste))



# exo 4
def exo4():
    p = 0.9
    x = 2
    f = "p**x - (1/x)"
    e = "p**(x+1) - (1/(x+1))"
    while eval(e) > eval(f):
        x += 1
    print(eval(e),   eval(f),  x) 

def exo5():
    
    tarifs = ["bleu", "vert", "orange" ,"rouge"]
    tarif = ""
    age, temps_permis,accident, assurance, satisfait = 26, 3, 0, 1, 6
    
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
    print(tarif)
    


    
        
        
            
    
    
    



