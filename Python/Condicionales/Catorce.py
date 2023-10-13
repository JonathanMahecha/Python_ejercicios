#El número de pulsaciones que debe tener una persona por cada 10 segundos de ejercicio aeróbico se calcula con la fórmula:

edad = int(input("Ingrese su edad: "))
genero = int(input("Ingrese su género\n1 para femenino\n2 para masculino: "))

if genero == 1:
    pulsaciones = (220 - edad) / 10
    print(f"El número de pulsaciones: {pulsaciones} en 10 segundos de ejercicio")
elif genero == 2:
    pulsaciones = (210 - edad) / 10
    print(f"El número de pulsaciones: {pulsaciones} en 10 segundos de ejercicio")
else:
    print("Opción de género inválida.")
