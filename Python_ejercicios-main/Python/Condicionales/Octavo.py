#Solicitar tres números al usuario e imprimirlos en orden ascendente y descendente. 

print("Ingrese los siguientes números para empezar a operar")

num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))
num3 = float(input("Tercer número: "))

print("Ascendente:")

if num1 <= num2 <= num3:
    print(f"{num1} {num2} {num3}")
elif num1 <= num3 <= num2:
    print(f"{num1} {num3} {num2}")
elif num2 <= num1 <= num3:
    print(f"{num2} {num1} {num3}")
elif num2 <= num3 <= num1:
    print(f"{num2} {num3} {num1}")
elif num3 <= num1 <= num2:
    print(f"{num3} {num1} {num2}")
else:
    print(f"{num3} {num2} {num1}")

print("Descendente:")

if num1 >= num2 >= num3:
    print(f"{num1} {num2} {num3}")
elif num1 >= num3 >= num2:
    print(f"{num1} {num3} {num2}")
elif num2 >= num1 >= num3:
    print(f"{num2} {num1} {num3}")
elif num2 >= num3 >= num1:
    print(f"{num2} {num3} {num1}")
elif num3 >= num1 >= num2:
    print(f"{num3} {num1} {num2}")
else:
    print(f"{num3} {num2} {num1}")
