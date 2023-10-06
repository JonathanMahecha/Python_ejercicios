#Crear un programa con un menú de opciones, que permita calcular 
#las áreas de figuras geométricas (cuadrado, rectángulo, triángulo, círculo, rombo y trapecio).

print("Ingrese un número para comenzar a operar: ")

numero1 = int(input("Escriba un número de la lista: "))
print("0. Rectángulo\n1. Cuadrado\n2. Paralelogramo\n3. Rombo\n4. Trapecio\n5. Triángulo\n6. Triángulo equilátero\n7. Polígono Regular")

if numero1 == 0:
    numero2 = float(input("Ingrese el valor de 'a': "))
    numero3 = float(input("Ingrese el valor de 'b': "))
    area = numero2 * numero3
    print(f"El área del rectángulo es: {area}")
elif numero1 == 1:
    numero2 = float(input("Ingrese el valor de 'a': "))
    area = numero2 ** 2
    print(f"El área del cuadrado es: {area}")
elif numero1 == 2:
    numero2 = float(input("Ingrese el valor de 'b': "))
    numero3 = float(input("Ingrese el valor de 'h': "))
    area = numero2 * numero3
    print(f"El área del paralelogramo es: {area}")
elif numero1 == 3:
    numero2 = float(input("Ingrese el valor de 'a': "))
    numero3 = float(input("Ingrese el valor de 'c': "))
    numero4 = float(input("Ingrese el valor de 'b': "))
    numero5 = float(input("Ingrese el valor de 'd': "))
    area = (numero2 * numero4 * numero3 * numero5) / 2
    print(f"El área del rombo es: {area}")
elif numero1 == 4:
    numero2 = float(input("Ingrese el valor de 'a': "))
    numero3 = float(input("Ingrese el valor de 'c': "))
    numero4 = float(input("Ingrese el valor de 'h': "))
    area = ((numero2 + numero3) / 2) * numero4
    print(f"El área del trapecio es: {area}")
elif numero1 == 5:
    numero2 = float(input("Ingrese el valor de 'a': "))
    numero3 = float(input("Ingrese el valor de 'h': "))
    area = ((numero2 * numero3) / 2)
    print(f"El área del triángulo es: {area}")
elif numero1 == 6:
    numero2 = float(input("Ingrese el valor de 'a': "))
    area = ((numero2 ** 2 * (3 ** 0.5)) / 2)
    print(f"El área del triángulo equilátero es: {area}")
elif numero1 == 7:
    numero2 = float(input("Ingrese el valor de 'a': "))
    numero3 = float(input("Ingrese el valor de 'p': "))
    area = ((numero2 * numero3 ** numero3) / 2)
    print(f"El área del polígono regular es: {area}")
else:
    print("Opción no válida")
