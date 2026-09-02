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