import keyboard
import time

def demander_expression() :

    nombre1 = input("\nPremier nombre ? :\n")
    if not nombre1.replace(".", "", 1).isnumeric() :
        print("L'opération est impossible (Pas un nombre)")
        exit()

    nombre2 = input("\nSecond nombre ? :\n")
    
    if not nombre2.replace(".", "", 1).isnumeric() :
        print("L'opération est impossible (Pas un nombre)")
        exit()

    print("\nSéléctionner une expression : ")
    print("a. Addition")
    print("b. Soustraction")
    print("c. Multiplication")
    print("d. Division")
        
    while True :
        if keyboard.is_pressed("a") :
            return (nombre1, '+', nombre2)
        if keyboard.is_pressed("b") :
            return (nombre1, '-', nombre2)
        if keyboard.is_pressed("c") :
            return (nombre1, '*', nombre2)
        if keyboard.is_pressed("d") :
            if (float(nombre2)==(0)) :
                print("\nL'opération est impossible (Division par 0)\n")
                time.sleep(1)
                exit()
            return (nombre1, '/', nombre2)

###########################################

expression = demander_expression()
print(f"\nVoici l'expression :\n{expression[0]} {expression[1]} {expression[2]}")
print(f"\nRésultat :")
if (expression[1] == '+') :
    res = float(expression[0]) + float(expression[2])
    print(round(res, 3))
elif (expression[1] == '-') :
    res = float(expression[0]) - float(expression[2])
    print(round(res, 3))
elif (expression[1] == '*') :
    res = float(expression[0]) * float(expression[2])
    print(round(res, 3))
elif (expression[1] == '/') :
    res = float(expression[0]) / float(expression[2])
    print(round(res, 3))
else :
    print("ERREUR")