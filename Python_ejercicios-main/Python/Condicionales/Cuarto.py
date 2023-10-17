#Solicitar dos números al usuario y calcular cuál es el mayor y cuál el menor, e imprimir el resultado.

numero1 = int(input("Ingrese el numero 1: "))
numero2 = int(input("Ingrese el numero 2: "))

if numero1 < numero2: print(f" {numero2} es mayor que {numero1} ")
elif numero2 < numero1: print(f" {numero1} es mayor que {numero2} ")
