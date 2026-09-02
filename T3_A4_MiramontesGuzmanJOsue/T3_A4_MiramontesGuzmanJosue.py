print ("Este programa encuentra los divisores de un número.")
Numero = (int(input("Ingresa el valor para buscar sus divisores: ")))

divisores = [i for i in range (1, Numero + 1) if Numero % i == 0]
print (divisores)



print ("Este programa imprime un nombre la cantidad de veces que mida ese nombre.")
Nombre = input ( "Ingresa un nombre para imprimir la cantidad de veces que mida ese nombre:  ") #2
contador = len(Nombre)

for i in range(contador):
    print(Nombre)



print("Este programa multiplica una figura por un número de veces.")
figura = input("Ingresa una figura:  ") #2
Lineas = int(input("Ingresa la altura que te gustaria que tenga la figura:  "))
contador = len(figura) 

for i in range(Lineas):
    print(figura * 10)



print ("Este programa cuenta la cantidad de consonantes y vocales en un texto ingresado por el usuario.")
texto = input("Ingrese un texto: ")
consonantes = "bcdfghjklmnñpqrstvwxyz"
vocales = "aeiou"
contador = 0
contadorvocales = 0

for letra in texto.lower():
    if letra in consonantes:
        contador += 1
for letra in texto.lower():
    if letra in vocales:
        contadorvocales += 1
print("LAS CONSONANTES SON",contador)  # Resultado: 5 (h, l, m, n, d)
print("LA CANTIDAD DE VOCALES ES", contadorvocales)  # Resultado: 3 (a, e, i)

print ("Este programa cuenta la cantidad de consonantes, vocales, números y caracteres especiales en un texto ingresado por el usuario.")
texto = input("Ingrese un texto: ")
consonantes = "bcdfghjklmnñpqrstvwxyz"
vocales = "aeiou"
numeros = "0123456789"
caracteresespeciales = "!@#$%^&*()_+-=~`[]{}|;:'\",.<>?/"
contador_numeros = 0
contador_caracteres_especiales = 0
contador = 0
contadorvocales = 0


for letra in texto.lower():
    if letra in caracteresespeciales:
        contador_caracteres_especiales += 1
for letra in texto.lower():
    if letra in numeros:
        contador_numeros += 1
for letra in texto.lower():
    if letra in vocales:
        contadorvocales += 1
print("LAS CONSONANTES SON",contador)  # Resultado: 5 (h, l, m, n, d)
print("LA CANTIDAD DE VOCALES ES", contadorvocales)  # Resultado: 3 (a, e, i)
print("LA CANTIDAD DE NUMEROS ES", contador_numeros)  # Resultado: 3 (1, 2, 3)
print("LA CANTIDAD DE CARACTERES ESPECIALES ES", contador_caracteres_especiales)  # Resultado: 3 (!, @, #)