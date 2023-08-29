# Fonction pour additionner deux nombres
def addition(a, b):
    return a + b

# Fonction pour soustraire deux nombres
def soustraction(a, b):
    return a - b

# Fonction pour multiplier deux nombres
def multiplication(a, b):
    return a * b

# Fonction pour diviser deux nombres
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Erreur: Division par zéro"

# Boucle principale du programme
while True:
    print("Sélectionnez une opération:")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("0. Quitter")

    choix = input("Entrez votre choix (0-4): ")

    # Vérifier si l'utilisateur souhaite quitter le programme
    if choix == "0":
        print("Au revoir!")
        break

    # Demander à l'utilisateur d'entrer deux nombres
    nombre1 = float(input("Entrez le premier nombre: "))
    nombre2 = float(input("Entrez le deuxième nombre: "))

    # Effectuer l'opération sélectionnée
    if choix == "1":
        resultat = addition(nombre1, nombre2)
    elif choix == "2":
        resultat = soustraction(nombre1, nombre2)
    elif choix == "3":
        resultat = multiplication(nombre1, nombre2)
    elif choix == "4":
        resultat = division(nombre1, nombre2)
    else:
        print("Choix invalide")
        continue

    # Afficher le résultat
    print("Le résultat est:", resultat)
