

P_HORA = float(input("Ingresa el pago por hora:"))

while P_HORA < 0:
    print ("Error: No se permiten numero negativos.")
    P_HORA = float(input("Ingresa el pago por hora:"))
		
HORA_NORMAL =  int(input("Ingresa total de horas:"))

while HORA_NORMAL < 0:
    print ("Error: No se permiten numero negativos.")
    HORA_NORMAL =  int(input("Ingresa total de horas:"))

HORA_EXTRA = int(input("Ingresa las horas extra:"))
while HORA_EXTRA < 0:
    print ("Error: No se permiten numero negativos.")
    HORA_EXTRA = int(input("Ingresa las horas extra:"))

tipo_trabajador = int(input("Ingresa 1 trabajador normal o 2 si es supervisor:"))
while tipo_trabajador not in [1, 2]:
    print ("Error: Solo 1 o 2.")	
    tipo_trabajador = int(input("Ingresa 1 trabajador normal o 2 si es supervisor:"))

ANTIGUEDAD = int(input("Ingresa la antigüedad del trabajador: "))
while ANTIGUEDAD < 0:
    print ("Error: No se permiten numero negativos.")
    ANTIGUEDAD = int(input("Ingresa la antigüedad del trabajador: "))


IMPUESTOS = P_HORA * 0.26

if HORA_EXTRA >= 5 : 
    PAGO_HREXTRA = 3 * HORA_EXTRA
else: 
    PAGO_HREXTRA = 2 * HORA_EXTRA

if tipo_trabajador == 2 :
    if HORA_EXTRA >= 5 : 
      PAGO_HREXTRA = 3 * HORA_EXTRA
    else: 
      PAGO_HREXTRA = 2 * HORA_EXTRA

if tipo_trabajador == 1:
    SUELDOFINAL= ((P_HORA * HORA_NORMAL) + PAGO_HREXTRA) - IMPUESTOS
else:
    SUELDO = (P_HORA * HORA_NORMAL) + PAGO_HREXTRA
    BONO = SUELDO * 0.5
    SUELDOFINAL = SUELDO + BONO - IMPUESTOS
print(f"Sueldo final: {SUELDOFINAL}")


	