while True:
	try:
		subtotal = float(input("Ingrese el subtotal de la cuenta: "))
		break
	except ValueError:
		print("Ingrese un número decimal valido sin signo de dolar")

while True:
	tipo_cliente = input("Tipo de entrada (vip/normal): ").lower().strip()
	if tipo_cliente in ("vip", "normal"): 
		break
	print ("Entrada no válida, escriba 'vip' o 'normal'")
if tipo_cliente == "vip": 
	descuento = 0.15*subtotal
elif tipo_cliente == "normal" and subtotal >= 100: 
	descuento = 0.05*subtotal
else:
	descuento = 0*subtotal
total_final = subtotal - descuento

print (f"Subtotal: {subtotal}")
print (f"Descuento: {descuento}")
print (f"Total final: {total_final}")
