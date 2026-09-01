##vLeer un numero entero e indicar si es par o impar.
from xmlrpc.client import boolean

print("_________________PAR O IMPAR__________________")
Numero_int = int(input("Ingrese un número entero: "))

if Numero_int % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")


##Leer una cantidad de grados FAHRENHEIT y convertirlos a CENTÍGRADOS, si la temperatura convertida es menor a 0, mostrar &quot;CONGELANTE&quot;, en caso contrario mostrar &quot;NORMAL&quot;
print("_________________FAHRENHEIT A CENTIGRADOS__________________")
Temperatura = float(input("Ingrese la temperatura en grados Fahrenheit: "))
Centigrados = (Temperatura - 32) * 5 / 9
print ("La temperatura en grados Centigrados es:", Centigrados)
if Centigrados < 0:
    print("CONGELANTE")
else:
    print("NORMAL")


##
print ("_________________-Calculadora de salario neto__________________")
pago_hora = float(input("Ingresa el pago por hora: "))
dias_trabajados = int(input("Ingresa los días trabajados: "))
dias_extras = int(input("Ingresa los días extras: "))

salario_normal = (dias_trabajados * 8) * pago_hora

if dias_extras <= 5:
    salario_extras = dias_extras * pago_hora * 2
else:
    salario_extras = dias_extras * pago_hora * 3

salario_bruto = salario_normal + salario_extras
if salario_bruto > 20000:
    ispt = salario_bruto * 0.26
else:
    ispt = salario_bruto * 0.14
salario_neto = salario_bruto - ispt

print("El salario neto es:", salario_neto)

#Crear un programa que pida al usuario una temperatura en grados 
# centígrados y después pregunte al usuario si desea convertir a
#  grados Fahrenheit o grados Kelvin; dependiendo de la opción elegida, 
# pedir los datos necesarios para obtener dicha conversión  y mostrar le resultado en pantalla.


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




#Programa que lea tres números e indicar cual es el mayor.
print("_________________MAYOR DE TRES NÚMEROS__________________")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

if num1 >= num2 and num1 >= num3:
    print("El primer número es el mayor:", num1)
elif num2 >= num1 and num2 > num3:
    print("El segundo número es el mayor:", num2)
else:
    print("El tercer número es el mayor:", num3)


