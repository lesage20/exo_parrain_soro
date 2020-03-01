# exo 3
def exo3():
    n = 0
    liste = [n]
    a = input("entrez un nombre: ")
    a = int(a)
    while sum(liste) < int(a) + 1 :
        n = n + 1
        liste.append(n)
    print(f"Le plus petit entier est : {n} et Hn = ", sum(liste))
exo3()