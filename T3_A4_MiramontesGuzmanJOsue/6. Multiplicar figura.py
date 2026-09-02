
print("Este programa multiplica una figura por un número de veces.")
figura = input("Ingresa una figura:  ") #2
Lineas = int(input("Ingresa la altura que te gustaria que tenga la figura:  "))
contador = len(figura) 

for i in range(Lineas):
    print(figura * 10)