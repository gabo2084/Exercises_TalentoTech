#Registrar los ingresos mensuales de un cliente durante 6 meses usando un bucle while para solicitar el ingreso de cada mes. Validar que los ingresos sean números positivos. 
#Si se ingresa un valor negativo, mostrá un mensaje indicando que el valor no es válido y volvé a pedir el dato.
#Calcular el total acumulado durante los 6 meses y el promedio mensual. Mostrá este resultado al final del programa.

mes_ahorro = 0
meses_ahorro = 6
ahorro_total = 0

while mes_ahorro < meses_ahorro:

    ahorro_mensual = input(f'Ingrese el importe ahorrado del {mes_ahorro + 1} mes: $ ')

    if not ahorro_mensual.isnumeric() or ahorro_mensual == '':
        print("Por favor, ingresa un importe valido.")
        continue
    else:
        ahorro_mensual = float(ahorro_mensual)
        ahorro_total = ahorro_total + ahorro_mensual
        print(f'Ahorro del mes {mes_ahorro + 1}: $ {ahorro_mensual}')
        mes_ahorro = mes_ahorro + 1
        

print(f'El ahorro acumulado de los ultimos {meses_ahorro} meses es $ {ahorro_total}')
print(f'El promedio mensual ahorrado es de $ {round((ahorro_total / meses_ahorro), 2)}')

        
