#Calcular la hipotenusa con el Teorema de Pitágoras.

cateto1 = float(input("Ingrese la longitud del primer cateto: "))
cateto2 = float(input("Ingrese la longitud del segundo cateto: "))

hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** 0.5

print(f"La hipotenusa es {hipotenusa}")
