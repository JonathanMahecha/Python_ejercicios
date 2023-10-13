#Escribe un programa para leer 10 números del teclado y encontrar su suma y promedio.

total = 0
for i in range (1, 11):
    numero = int(input(f"Ingrese el numero {i}: "))
    total += numero
    promedio = total / 10
        
print(f"El total de la suma es: {total}, el total del promedio es: {promedio}")