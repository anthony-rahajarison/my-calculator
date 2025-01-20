import keyboard
import time

# Liste pour stocker l'historique des calculs
historique = []

def menu(): # Afficher et lire les touches du menu
    print("=== Menu Principal ===")
    print("\nAppuyez sur 'e' pour afficher l'historique ,'f' pour effectuer un calcul ou 'q' pour quitter le programme.")
    while True:
        if keyboard.is_pressed("e"): # Affiche l'historique
            afficher_historique()
        elif keyboard.is_pressed("q"): # Quitte le programme
            exit()
        elif keyboard.is_pressed("f"): # Nouvelle opération
            operation()

def demander_expression():
    nombre1 = input("\nPremier nombre ? :\n")
    if not nombre1.replace(".", "", 1).isnumeric(): # Verifie si les entrées sont bien des nombres
        print("L'opération est impossible (Pas un nombre)")
        return demander_expression()

    nombre2 = input("\nSecond nombre ? :\n")
    if not nombre2.replace(".", "", 1).isnumeric(): # Verifie si les entrées sont bien des nombres
        print("L'opération est impossible (Pas un nombre)") 
        return demander_expression()

    print("\nSélectionner une opération : ")
    print("a. Addition")
    print("b. Soustraction")
    print("c. Multiplication")
    print("d. Division")
    print("e. Exposant")

    while True: # Boucle pour choix de l'opération
        if keyboard.is_pressed("a"):
            return (nombre1, '+', nombre2)
        if keyboard.is_pressed("b"):
            return (nombre1, '-', nombre2)
        if keyboard.is_pressed("c"):
            return (nombre1, '*', nombre2)
        if keyboard.is_pressed("d"):
            # Test de la division par 0
            if float(nombre2) == 0:
                print("\nL'opération est impossible (Division par 0)\n")
                time.sleep(1)
                return demander_expression()
            return (nombre1, '/', nombre2)
        if keyboard.is_pressed("e") : # Met le second nombre en exposant
            return (nombre1, '**', nombre2)

def afficher_historique():
    print("\n=== Historique des calculs ===")
    if not historique: # Si l'historique est vide
        print("Aucun calcul effectué pour le moment.")
    else:
        for num, calcul in enumerate(historique,start=1): # Affiche l'historique ligne par ligne
            print(f"{num}. {calcul}")

    print("Pour reintialiser, appuyez sur 'S' sinon appuyez sur 'P'.")

    while True:
        if keyboard.is_pressed("s"):
            time.sleep(0.5)
            print("'V' Réinitialiser entièrement\n'A' Supprimer une ligne")
            while True:
                if keyboard.is_pressed("a"):
                    try:
                        num_sup = int(input("Numéro du calcul à supprimer : ")) - 1
                        if num_sup < len(historique): # Si ligne du calcul existe
                            print(f"Suppression du calcul : {historique[num_sup]}")
                            historique.pop(num_sup)
                            time.sleep(0.5)
                            return menu()
                        else: # Si ligne de calcul n'éxiste pas
                            print("Numéro invalide.")
                            return afficher_historique()
                    except ValueError:
                        print("Entrée invalide.")

                if keyboard.is_pressed("v"):
                    historique.clear()
                    time.sleep(1)
                    return menu()

        if keyboard.is_pressed("p"): # Retour au menu
            input("\nAppuyez sur Entrée pour revenir au menu principal.")
            keyboard.is_pressed("Enter")
            return menu()
            


# Faire l'opération
def operation() :
    expression = demander_expression()

    print(f"\nVoici l'expression :\n{expression[0]} {expression[1]} {expression[2]}")
    print(f"\nRésultat :")

    if expression[1] == '+':
        res = float(expression[0]) + float(expression[2])
    elif expression[1] == '-':
        res = float(expression[0]) - float(expression[2])
    elif expression[1] == '*':
        res = float(expression[0]) * float(expression[2])
    elif expression[1] == '/':
        res = float(expression[0]) / float(expression[2])
    elif expression[1] == '**':
        res = 1
        for i in range(1, int(expression[2])+1) :
            res = res*int(expression[0])
    else:
        print("ERREUR")

    print(round(res,3)) # Arrondis le résultat
    time.sleep(1.0)

    # Ajouter l'expression et le résultat à l'historique
    historique.append(f"{expression[0]} {expression[1]} {expression[2]} = {res}")
    
    print("Appuyez sur entrée pour revenir au Menu")
    if keyboard.read_key("enter"):
        return menu()


###########################################

menu()