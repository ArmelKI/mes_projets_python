#1
def table(base, debut, fin, inc):
    """Cette procédure doit afficher la table des base, de debut à fin, de inc en inc"""
    for i in range(debut, fin+1, inc):
        print(f"{base} x {i} = {base*i}")

"""Programme principal"""
b= int(input("Entrez la base de la table: "))
d= int(input("Entrez le début de la table: "))
f= int(input("Entrez la fin de la table: "))
i= int(input("Entrez l'incrément: "))
table(b, d, f, i)

#2
def cube():
    n = int(input("Entrez un entier: "))
    """Cette fonction retourne le cube de n"""
    return n ** 3

from math import pi
def volumeSphere(r):
    """Cette fonction retourne le volume de la sphère de rayon r"""
    return (4/3) * pi * cube(r)

# Test de la fonction volumeSphere dans le programme principal
rayon = float(input("Entrez le rayon de la sphère: "))
print(f"Le volume de la sphère est {volumeSphere(rayon)}")

#3
import easygui

def maFonction(x):
    """Retourne la valeur de f(x) = 2x^3 + x - 5"""
    return 2 * x ** 3 + x - 5

def tabuler(fonction, borneInf, borneSup, nbpas):
    """Affiche la table de la fonction 'fonction' de borneInf à borneSup avec un pas 'nbpas'"""
    if borneInf >= borneSup:
        print("Erreur : borneInf doit être strictement inférieure à borneSup.")
        return
    if nbpas <= 0:
        print("Erreur : Le nombre de pas doit être un entier strictement positif.")
        return

    x = borneInf
    while x <= borneSup:
        print(f"f({x:.2f}) = {fonction(x): .4f}")
        x += nbpas

# Saisie des bornes et du pas avec easygui
bornes = easygui.multenterbox("Entrez les bornes inférieure et supérieure :", "Saisie des bornes", ["Borne inférieure", "Borne supérieure"])
if bornes:
    try:
        borneInf = float(bornes[0])
        borneSup = float(bornes[1])
    except ValueError:
        easygui.msgbox("Les bornes doivent être des nombres réels.", "Erreur")
    else:
        nbpas_str = easygui.enterbox("Entrez le pas (nombre réel positif) :", "Saisie du pas")
        if nbpas_str:
            try:
                nbpas = float(nbpas_str)
                if nbpas > 0:
                    tabuler(maFonction, borneInf, borneSup, nbpas)
                else:
                    easygui.msgbox("Le pas doit être un nombre réel strictement positif.", "Erreur")
            except ValueError:
                easygui.msgbox("Le pas doit être un nombre réel.", "Erreur")

