# Obtener el promedio dè N Calificaciones ingresadas por el usuario

n = int(input("Ingresa el número de calificaciones: "))

total = 0
for i in range(n):
    calificacion = int(input(f"Ingresa la calificación {i+1}: "))
    if calificacion < 0 or calificacion > 100:
        print("La calificación debe estar entre 0 y 100. Intenta de nuevo.")
        calificacion = int(input(f"Ingresa la calificación {i+1}: "))
    total += calificacion   

promedio = total / n
print("El promedio es:", promedio)



## Imprimir una tabla de multiplicar ingresada por el usuario
print("\nTabla de multiplicar")
numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
LIMITE = int(input("Ingresa hasta qué número quieres multiplicar: "))
for i in range(1, LIMITE+1):
    print(f"{numero} x {i} = {numero * i}")

### Imprimir una tabla de multiplicar del NUMERO que el usuario ingrese, hasta el LIMITE que el usuario ingrese
print("\nTabla de multiplicar")
numero = int(input("Ingresa un número para iniciar su tabla de multiplicar: "))
liValTable = int(input("Ingresa hasta qué número quieres multiplicar: "))
if numero <= litValTable:
    for i in range(numero, liValTable + 1):
        #print(f"{numero} x {i} = {numero * i}")
    LIMITE = int(input("Ingresa el limite del número quieres multiplicar: "))
    for i in range(numero, LIMITE + 1):
        print(f"{numero} x {i} = {numero * i}")
else:
    print("El programa ha finalizado")