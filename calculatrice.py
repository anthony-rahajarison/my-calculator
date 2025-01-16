import keyboard
import time

# Liste pour stocker l'historique des calculs
historique = []

def demander_expression():
    nombre1 = input("\nPremier nombre ? :\n")
    if not nombre1.replace(".", "", 1).isnumeric():
        print("L'opération est impossible (Pas un nombre)")
        demander_expression()

    nombre2 = input("\nSecond nombre ? :\n")
    if not nombre2.replace(".", "", 1).isnumeric():
        print("L'opération est impossible (Pas un nombre)")
        demander_expression()

    print("\nSélectionner une opération :")
    print("a. Addition")
    print("b. Soustraction")
    print("c. Multiplication")
    print("d. Division")

    while True:
        if keyboard.is_pressed("a"):
            return (nombre1, '+', nombre2)
        if keyboard.is_pressed("b"):
            return (nombre1, '-', nombre2)
        if keyboard.is_pressed("c"):
            return (nombre1, '*', nombre2)
        if keyboard.is_pressed("d"):
            if float(nombre2) == 0:
                print("\nL'opération est impossible (Division par 0)\n")
                time.sleep(1)
                demander_expression()
            return (nombre1, '/', nombre2)

def afficher_historique():
    print("\n=== Historique des calculs ===")
    if not historique:
        print("Aucun calcul effectué pour le moment.")
    else:
        for i, calcul in enumerate(historique,start=1):
            print(f"{i}. {calcul}")
    input("\nAppuyez sur Entrée pour revenir au menu principal.")
    keyboard.is_pressed("Enter")
    return menu()

###########################################
def menu():
    print("=== Menu Principal ===")
    print("\nAppuyez sur 'e' pour afficher l'historique ,'f' pour effectuer un calcul ou 'q' pour quitter le programme.")

menu()
while True:
    if keyboard.is_pressed("e"):
        afficher_historique()
    elif keyboard.is_pressed("q"):
        exit()
    elif keyboard.is_pressed("f"):
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
        else:
            print("ERREUR")
            continue

        print(round(res,3))
        time.sleep(2.0)
        print("Appuyez sur entrée pour revenir au Menu")
        if keyboard.read_key("enter"):
            menu()

        # Ajouter l'expression et le résultat à l'historique
        historique.append(f"{expression[0]} {expression[1]} {expression[2]} = {res}")