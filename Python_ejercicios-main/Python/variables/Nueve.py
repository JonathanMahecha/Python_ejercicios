#Programa que permita a una tienda saber el valor que pagara un cliente por la compra de varios elementos de la misma referencia. 
#Debe tener como entradas el valor unitario, la cantidad de productos comprados y al valor final se debe adicionar el 16% correspondiente al IVA.

producto = int(input("Ingrese la cantidad de productos: "))
valor = int(input("Ingrese el valor de los productos: "))
total = (producto*valor)
iva = ((total*16)/100)
final = iva + total
print(f"El total de los productos sin iva es: {total} y con el iva aplicado es: {final}")