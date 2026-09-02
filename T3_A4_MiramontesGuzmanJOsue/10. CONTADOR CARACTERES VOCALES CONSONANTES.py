print ("CONTADOR DE CARACTERES, VOCALES, CONSONANTES, NUMEROS Y CARACTERES ESPECIALES")
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