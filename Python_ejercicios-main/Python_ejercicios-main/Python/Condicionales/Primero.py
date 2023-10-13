#Solicitar número al usuario y determinar si es par, impar o es cero. 

numero = int(input("Ingrese el numero el cual desea saber si es entero o impar: "))

if numero == 0: print("El numero es igual a 0")
elif numero % 2 == 0: print("El numero es par")
else: print("El numero es impar")