#Contrôle du flux d’instructions 

#1
flottant= float(input("Entrez un nombre flottant: "))
if flottant >= 0:
    print(f" La racine carrée de {flottant} est {flottant**0.5}")
else:
    print("Le nombre doit être positif")
#2
mot1= input("Entrez un mot: ")
mot2= input("Entrez un autre mot: ")
if len(mot1) < len(mot2):
    print(f"Le mot le plus long est {mot2}")
elif len(mot1) > len(mot2):
    print(f"Le mot le plus long est {mot1}")
else:
    print("Les deux mots ont la même longueur")
#3
pSeuil= 2.3
vSeuil= 7.41
p= float(input("Entrez la pression: "))
v= float(input("Entrez le volume: "))
if p > pSeuil and v > vSeuil:
    print("ARRET IMMEDIAT")
elif v> vSeuil:
    print("Diminuer le volume")
else:
    print("Tout va bien")
#4
a= 0
b= 10
while a<b:
    print(a)
    a+= 1

while b%2 != 0 and b>0:
    print(b)
    b-= 1

#5
import random
mot= input("Entrez un mot: ")
for _ in mot:
    print(_)

liste= random.sample(range(1, 101), 10)
for _ in liste:
    print(_)

#6
for i in range(1, 15, 3):
    print(i)

#7
for i in range(10):
    if i ==5:
        break
    print(i)

#8
#Utilisez l’instruction break pour interrompre une boucle for d’affichage des entiers de 1 à 10 compris, lorsque la variable de boucle vaut 5
for i in range(10):
    if i ==5:
        continue
    print(i)

#9
# Utilisez une exception pour calculer, dans une boucle évoluant de -3 à 3 compris, la valeur de sin(x)/x.
import math
for x in range(-3, 4):
    try:
        result = math.sin(x) / x
    except ZeroDivisionError:
        result = "indéfini"
    print(f"x={x}, sin(x)/x={result}")

#10
# Utilisation de la clause else dans les boucles
import easygui
# Partie 1 : Recherche d'un entier dans une liste
liste = [3, 7, 12, 18, 25]
entier = easygui.integerbox("Entrez un entier :", "Recherche dans la liste")
for val in liste:
    if val == entier:
        easygui.msgbox(f"{entier} appartient à la liste.", "Résultat")
        break
else:
    easygui.msgbox(f"{entier} ne se trouve pas dans la liste.", "Résultat")

# Partie 2 : Vérification si un entier est premier
n = easygui.integerbox("Entrez un entier positif :", "Test de primalité")
if n is None or n < 2:
    easygui.msgbox("Le nombre doit être supérieur ou égal à 2.", "Erreur")
else:
    i = 2
    while i <= int(n ** 0.5):
        if n % i == 0:
            easygui.msgbox(f"{n} n'est pas premier, diviseur trouvé : {i}")
            break
        i += 1
    else:
        easygui.msgbox(f"{n} est un nombre premier.", "Résultat")