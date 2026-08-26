##Instrucciones: Desarrollar los siguientes programas en PYTHON:
##1. Crear un programa que describa los pasos para sumar dos números enteros.
##2. Crear un programa que describa los pasos para obtener el área de un triángulo.
##3. Escribir un programa para obtener la edad de una persona con base en su año de nacimiento.
##4. Crear un programa para obtener el área de un círculo.
##5. Diseñar un programa que muestre el promedio de 5 calificaciones.

##Para sumar dos números enteros, se deben seguir los siguientes pasos:
##   1. Ingresar el primer número.
##   2. Ingresar el segundo número.
##   3. Sumar ambos números.
##   4. Mostrar el resultado de la suma.
import math


print ("Calcular la suma de dos números enteros:")
a = 1
b = 2
suma = a + b
print(suma)

###Para obtener el área de un triángulo, se deben seguir los siguientes pasos:
##   1. Ingresar la base del triángulo.
##   2. Ingresar la altura del triángulo.
##   3. Calcular el área utilizando la fórmula: área = (base * altura
print ("calcular el área de un triángulo:")
base = 2
altura = 3
area = (base * altura) / 2
print(area)

###Para obtener la edad de una persona con base en su año de nacimiento, se deben seguir los siguientes pasos:
## 1. Ingresar el año de nacimiento de la persona.
## 2. Calcular la edad restando el año de nacimiento al año actual.
print ("Calcular la edad de una persona con base en su año de nacimiento:")
print ("Ingrese su año de nacimiento:")
anio_nacimiento = int(input())
anio_actual = 2026
edad = anio_actual - anio_nacimiento
print ("tU ANIO DE NACIMIENTO ES: " + str(edad))

##Para obtener el area de un circulo
##Para sacar el área de un círculo debes multiplicar el valor de pi (\(\pi \)) por el radio al cuadrado (\(\text{Área} = \pi \times r^2\)).
print("Calcular el área de un círculo:")
pi = 3.14159
print ("Ingrese el radio del círculo:")
radio = float(input())
area_circulo = pi * (radio ** 2)
print ("El área del círculo es: " + str(area_circulo))

##6. Crear un programa que solucione la ecuación cuadrática.
##7. Escribir un programa que pida una distancia dada en Millas y muestre su valor en Kilómetros, Metros y centímetros.
##8. Crear un programa que pida una cantidad de grados Centígrados y los convierta en grados Fahrenheit y grados Rankin
##9. Diseñar un programa que convierta una cantidad dada en segundos a su tiempo en horas, minutos y segundos sobrantes.
##10. Crear un programa que calcule el salario neto de una persona con base en las siguientes características:

##PARA SOLUCIONAR LA ECUACION CUADRATICA, SE DEBEN SEGUIR LOS SIGUIENTES PASOS:
## ingresar los valores de a, b y c de la ecuación cuadrática ax^2 + bx + c = 0.
print ("Calcular la ecuación cuadrática:")

##DEFINIR LOS VALORES DE a, b y c
a = float(input("Ingresse el valor de a:"))
b = float(input("Ingresse el valor de b:"))
c = float(input("Ingresse el valor de c:"))


discriminante = (b**2) - (4*a*c)
if discriminante <= 0:
    print("La ecuación no tiene soluciones reales.")
else:
    RAIZ =math.sqrt((b**2) - (4*a*c))
    FORMULA2 = ((-b - RAIZ)/2 * a)
    FORMULA1 = ((-b + RAIZ)/2 * a)

print (f"El valor de {FORMULA1} y {FORMULA2}")

 ##crear un programa que pida una cantidad de grados Centígrados y los convierta en grados Fahrenheit y grados Rankin
##(0 * 9/5) + 32 = 32 
## Declarar una variable para almacenar la temperatura en grados Celsius
print ("Convertir grados Celsius a Fahrenheit y Rankin:")
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
CONVERTIR_FAREHEIT = (celsius * 9/5) + 32
CONVERTIR_RANKIN = (celsius + 273.15) * 9/5
print(f"{celsius} °C son {CONVERTIR_FAREHEIT} F y {CONVERTIR_RANKIN} °R")


##Salario Bruto = horas trabajadas * precio por hora + horas Extras
##      Horas extras = horas extra trabajadas * (precio por hora * 2)
 ##   Salario Neto = salario bruto – IVA – impuestos

##inGRESAR PRECIO POR HORA
## INGRESAR HORAS TRABAJADAS 
## INGRESAR HORAS EXTRAS
## INGRESAR IVA
## INGRESAR IMPUESTOS

print("CALCULAR SALARIO NETO")
HORAS_TRABAJADAS = float(input("Ingrese las horas trabajadas: "))
PRECIO_POR_HORA = float(input("Ingrese el precio por hora: "))
HORASEXTRA_CANTIDAD = float(input("Ingrese las horas extras trabajadas: "))
HORASEXTRA_VALOR = PRECIO_POR_HORA * 2
SALARIOBRUTO = (HORAS_TRABAJADAS * PRECIO_POR_HORA) + (HORASEXTRA_VALOR * (HORASEXTRA_CANTIDAD))
IVA = SALARIOBRUTO * 0.16
ISR = SALARIOBRUTO * 0.30
RESICO = SALARIOBRUTO * 0.025
IMPUESTOS = ISR + RESICO 
SALARIONETO = SALARIOBRUTO - IVA - IMPUESTOS


print("Tu pago total es: " + str(SALARIONETO))



