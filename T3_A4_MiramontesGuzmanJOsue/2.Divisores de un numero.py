print ("Este programa encuentra los divisores de un número.")
Numero = (int(input("Ingresa el valor para buscar sus divisores: ")))

divisores = [i for i in range (1, Numero + 1) if Numero % i == 0]
print (divisores)
