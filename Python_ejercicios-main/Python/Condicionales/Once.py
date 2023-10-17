#El precio que debe pagar un cliente por una pizza depende del tamaño seleccionado, como se muestra a continuación:

tamano_pizza = int(input("Ingrese el tamaño de la pizza:\n1. $15,000\n2. $24,000\n3. $36,000: "))

precio_base = 0

if tamano_pizza == 1:
    precio_base = 15000
elif tamano_pizza == 2:
    precio_base = 24000
elif tamano_pizza == 3:
    precio_base = 36000
else:
    print("Tamaño de pizza inválido")

if precio_base > 0:
    num_ingredientes = int(input("Ingrese el número de ingredientes adicionales: "))
    precio_ingredientes = num_ingredientes * 4000
    precio_total = precio_base + precio_ingredientes
    print(f"Precio total a pagar: ${precio_total} COP")
