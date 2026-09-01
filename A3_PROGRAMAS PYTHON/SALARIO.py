
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
