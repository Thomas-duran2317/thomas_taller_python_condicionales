while True:
    try:
        distancia = float(input("Ingrese la distancia recorrida en km: "))
        break
    except ValueError:
        print ("Ingrese un valor decimal valido sin 'km'")

while True:
    try:
        hora = int(input("Ingrese la hora de viaje (valor aceptable de 0 horas a 23 horas): "))
        if hora>=0 and hora<=23:
            break
        else:
            print ("Ingresar un valor entre 0 a 23")
    except ValueError:
        print ("Ingresar un valor entero sin dar los minutos")

costo_fijo = 1

if hora >= 6 and hora <=19:
    horario = 'Diurno'
    costo_marginal = 0.50*distancia

if hora >= 20 and hora <=23 or hora >= 0 and hora <=5:
    horario = 'Nocturno'
    costo_marginal = 0.65*distancia

if distancia>=10:
    costo_fijo_2 = 2
else:
    costo_fijo_2 = 0

costo_total = costo_fijo + costo_marginal + costo_fijo_2

print ("TARIFA DE TAXI")
print ("-----------------")
print (f"Horario: {horario}")
print (f"Distancia {distancia} km")
print (f"Costo total ${costo_total:.2f}")
