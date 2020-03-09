from collections import deque

def exo1():
    n = 0
    while n not in range(1,4):
        n = input("Veuillez entrer un nombre: ") 
        n = int(n)
    print("Bravo ")


def exo2():
    
    while True:
        n= int(input("Veuillez saisir un nombre: "))
        if 10 <= n <= 20:
            print("bravo")
            break
        if n < 10:
            print("Svp veuillez saisir un nombre plus grand ")
        elif n > 20:
            print("Svp veuillez saisir un nombre plus petit ")

def exo3():
    n_initial = int(input("veuillez entrer un nombre: "))
    n = n_initial
    
    while n <= n_initial + 9:
        n = n + 1
        print(n)

def exo4():
    n_initial = int(input("veuillez entrer un nombre: "))
    for n in range(n_initial, n_initial + 10):
        print(n + 1)

def exo5():
    n_initial = int(input("veuillez entrer un nombre: "))
    print(f"Table de {n_initial} est: ")
    for n in range(1, 11):
        print(f"{n_initial} x {n} = {n_initial * n}")

def exo6():
    n_initial = int(input("veuillez entrer un nombre: "))
    print(sum(range(1,n_initial + 1)))

def exo6():
    n_initial = int(input("veuillez entrer un nombre: "))
    som = 0
    for i in range(1, n_initial + 1):
        som += i      
    print(som)
    
def exo7():
    n_initial = int(input("veuillez entrer un nombre: "))
    fact = 1
    for i in range(1, n_initial + 1):
        fact *= i  
    print(f"factoriel de {n_initial} est : {fact}")
        
def exo8():
    liste  = []
    for i in range(1, 21):
        dicto  = {f"n{i}" : int(input(f"veuillez saisir le nombre numero {i}: "))} 
        liste.append(dicto[f"n{i}"])
    
    print(f"le plus grand nombre entré est : {max(liste)}, \nC'etait le nombre numero {liste.index(max(liste)) + 1}")
    

def exo9():
    liste = []
    print("entrez 0 si vous avez fini de saisir")
    while True:
        n = int(input("Veuillez saisir un nombre: "))
        if n == 0:
            print(f"le plus grand nombre entré est : {max(liste)}, \nC'etait le nombre numero {liste.index(max(liste)) + 1}")
            break 
        else:
            liste.append(n)

def exo10():
    nombre = 1
    somme = 0
    montant_verse = ''

    while 1:
        nombre = input("Entrez le montant : ")
        if nombre.isdigit():
            if int(nombre) == 0:
                break
            somme += int(nombre)

    print("\nVous devez:", somme, "euros\n")

    while not montant_verse.isdigit():
        montant_verse = input("Montant verse: ")

    reste = int(montant_verse) - somme

    nb_10_euros = reste // 10
    nb_5_euros = (reste % 10) // 5
    nb_1_euros = (reste % 10) % 5

    print("\nMonnaie a rendre: ")
    print("Billets de 10 €:", nb_10_euros)
    print("Billets de 5  €:", nb_5_euros)
            


