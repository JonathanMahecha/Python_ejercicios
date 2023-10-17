#Escriba un programa para mostrar la tabla de multiplicar de un entero dado.

total = 0
numero = int(input("Ingrese el numero del que desea conocer la tabla de multiplicar: "))
for i in range (1, 11):
    total += numero 
    total * i
    print(f"{numero} x {i} = {total}")
    