#Programa que permita determinar el salario a pagar a un empleado, teniendo como entradas el salario diario y el número de días trabajados. 
#Tenga en cuenta que al empleado se le debe descontar el 10% por concepto de pensión y 15% por concepto de salud.


pago_diario = int(input("Ingrese la cantidad de plata que gana diariamente: "))
dias_trabajados = int(input("Ingrese la cantidad de dias trabajados: "))
total = (pago_diario*dias_trabajados)
iva1 = ((total*10)/100)
iva2 = ((total*15)/100)
final = iva1 + total
final2 = iva2 + final
print(f"El total del pago sin el descontar es: {total} 10% por concepto de pensión es: {final} y 15% por concepto de salud {final2}")