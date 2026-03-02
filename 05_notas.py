while True:
    try:
        english = float(input("Ingresar su nota de inglés: "))
        if english >= 0 and english <= 100:
            break
        else:
            print ("Ingresar un valor entre 0 y 100: ")
    except ValueError:
        print ("Error: nota inválida. Ingresar un valor numérico decimal")

while True:
    try:
        math = float(input("Ingresar su nota de matemáticas: "))
        if math >= 0 and math <= 100:
            break
        else:
            print ("Ingresar un valor entre 0 y 100: ")
    except ValueError:
        print ("Error: nota inválida. Ingresar un valor numérico decimal")

while True:
    try:
        chemistry = float(input("Ingresar su nota de química: "))
        if chemistry >= 0 and chemistry <= 100:
            break
        else:
            print ("Ingresar un valor entre 0 y 100: ")
    except ValueError:
        print ("Error: nota inválida. Ingresar un valor numérico decimal")

promedio = (chemistry + math + english)/3

if promedio >=90 and promedio <=100:
    clasificación = 'Excelente'
elif promedio >=79 and promedio <90:
    clasificación = 'Muy bueno'
elif promedio >=70 and promedio <80:
    clasificación = 'Bueno'
elif promedio >=60 and promedio <70:
    clasificación = 'Supletorio'
else:
    clasificación = 'Reprobado'

print ("NOTAS FINALES")
print ("--------------")
print (f"Calificación inglés: {english}")
print (f"Calificación matemáticas: {math}")
print (f"Calificación química: {chemistry}")
print (f"Promedio: {promedio}")
print (f"Clasificación final: {clasificación}")
