print("_________________FAHRENHEIT A CENTIGRADOS__________________")
Temperatura = float(input("Ingrese la temperatura en grados Fahrenheit: "))
Centigrados = (Temperatura - 32) * 5 / 9
print ("La temperatura en grados Centigrados es:", Centigrados)
if Centigrados < 0:
    print("CONGELANTE")
else:
    print("NORMAL")

