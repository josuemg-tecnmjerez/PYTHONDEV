

print("_________________GRADOS CENTIGRADOS A FAREHHEIT__________________")
Temperatura = float(input("Ingrese la temperatura en grados Centigrados: "))

boolean = input("Desea convertir a Fahrenheit o Kelvin? (F/K): ")
if boolean == "F":
    F = (Temperatura * 1.8) + 32
    print("La temperatura en Fahrenheit es:", F)
elif boolean == "K":
    K = Temperatura + 273.15
    print("La temperatura en Kelvin es:", K)
else:
    print("Opción no válida")

if Centigrados < 0:
    print("CONGELANTE")
    F = ()
else:
    print("NORMAL")
