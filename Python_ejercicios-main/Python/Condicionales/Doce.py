#Un local vende sus productos con la siguiente promoción. Si compra hasta 5 artículos, no hay descuento. Si compra más de 5 artículos, pero menos de 10, el precio unitario se reduce en 5%. Si compra 10 o más artículos, el precio unitario se reduce en 8%. Ingrese un dato de cantidad y el valor del precio unitario original. Calcule y muestre el valor total a pagar.

cantidad = int(input("Ingrese la cantidad de artículos: "))
precio_unitario = float(input(f"Ingrese el precio unitario: $"))

if 5 < cantidad < 10:
    precio_unitario *= 0.95
elif cantidad >= 10:
    precio_unitario *= 0.92

valor_total = cantidad * precio_unitario

print(f"Valor total a pagar: ${valor_total:.2f} COP")
