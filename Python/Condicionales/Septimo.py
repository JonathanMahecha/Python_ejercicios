#Conversión de temperaturas. Crear un menú de opciones. 

print("CONVERSIÓN DE TEMPERATURAS")
print("1. Convertir de Celsius a Fahrenheit")
print("2. Convertir de Celsius a Kelvin")
print("3. Convertir de Celsius a Rankine")
print("4. Convertir de Celsius a Réaumur")
print("5. Convertir de Fahrenheit a Celsius")
print("6. Convertir de Fahrenheit a Kelvin")
print("7. Convertir de Fahrenheit a Rankine")
print("8. Convertir de Fahrenheit a Réaumur")
print("9. Convertir de Kelvin a Celsius")
print("10. Convertir de Kelvin a Fahrenheit")
print("11. Convertir de Kelvin a Rankine")
print("12. Convertir de Kelvin a Réaumur")
print("13. Convertir de Rankine a Celsius")
print("14. Convertir de Rankine a Fahrenheit")
print("15. Convertir de Rankine a Kelvin")
print("16. Convertir de Rankine a Réaumur")
print("17. Convertir de Réaumur a Celsius")
print("18. Convertir de Réaumur a Fahrenheit")
print("19. Convertir de Réaumur a Kelvin")
print("20. Convertir de Réaumur a Rankine")

opcion = int(input("Seleccione una opción: "))

if opcion == 1:
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit = round((celsius * 9 / 5) + 32, 2)
    print(f"{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit")
elif opcion == 2:
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    kelvin = round(celsius + 273.15, 2)
    print(f"{celsius} grados Celsius equivalen a {kelvin} grados Kelvin")
elif opcion == 3:
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    rankine = round((celsius + 273.15) * (9 / 5), 2)
    print(f"{celsius} grados Celsius equivalen a {rankine} grados Rankine")
elif opcion == 4:
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    reaumur = round(celsius * 0.8, 2)
    print(f"{celsius} grados Celsius equivalen a {reaumur} grados Réaumur")
elif opcion == 5:
    fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
    celsius = round((fahrenheit - 32) * 5 / 9, 2)
    print(f"{fahrenheit} grados Fahrenheit equivalen a {celsius} grados Celsius")
elif opcion == 6:
    fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
    kelvin = round((fahrenheit + 459.67) * 5 / 9, 2)
    print(f"{fahrenheit} grados Fahrenheit equivalen a {kelvin} grados Kelvin")
elif opcion == 7:
    fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
    rankine = round(fahrenheit + 459.67, 2)
    print(f"{fahrenheit} grados Fahrenheit equivalen a {rankine} grados Rankine")
elif opcion == 8:
    fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
    reaumur = round((fahrenheit - 32) * 4 / 9, 2)
    print(f"{fahrenheit} grados Fahrenheit equivalen a {reaumur} grados Réaumur")
elif opcion == 9:
    kelvin = float(input("Ingrese la temperatura en grados Kelvin: "))
    celsius = round(kelvin - 273.15, 2)
    print(f"{kelvin} grados Kelvin equivalen a {celsius} grados Celsius")
elif opcion == 10:
    kelvin = float(input("Ingrese la temperatura en grados Kelvin: "))
    fahrenheit = round((kelvin - 273.15) * 9 / 5 + 32, 2)
    print(f"{kelvin} grados Kelvin equivalen a {fahrenheit} grados Fahrenheit")
elif opcion == 11:
    kelvin = float(input("Ingrese la temperatura en grados Kelvin: "))
    rankine = round(kelvin * 9 / 5, 2)
    print(f"{kelvin} grados Kelvin equivalen a {rankine} grados Rankine")
elif opcion == 12:
    kelvin = float(input("Ingrese la temperatura en grados Kelvin: "))
    reaumur = round((kelvin - 273.15) * 4 / 5, 2)
    print(f"{kelvin} grados Kelvin equivalen a {reaumur} grados Réaumur")
elif opcion == 13:
    rankine = float(input("Ingrese la temperatura en grados Rankine: "))
    celsius = round((rankine - 491.67) * 5 / 9, 2)
    print(f"{rankine} grados Rankine equivalen a {celsius} grados Celsius")
elif opcion == 14:
    rankine = float(input("Ingrese la temperatura en grados Rankine: "))
    fahrenheit = round(rankine - 459.67, 2)
    print(f"{rankine} grados Rankine equivalen a {fahrenheit} grados Fahrenheit")
elif opcion == 15:
    rankine = float(input("Ingrese la temperatura en grados Rankine: "))
    kelvin = round(rankine * 5 / 9, 2)
    print(f"{rankine} grados Rankine equivalen a {kelvin} grados Kelvin")
elif opcion == 16:
    rankine = float(input("Ingrese la temperatura en grados Rankine: "))
    reaumur = round(((rankine - 491.67) * 4 / 9), 2)
    print(f"{rankine} grados Rankine equivalen a {reaumur} grados Réaumur")
elif opcion == 17:
    reaumur = float(input("Ingrese la temperatura en grados Réaumur: "))
    celsius = round((reaumur * 5 / 4), 2)
    print(f"{reaumur} grados Réaumur equivalen a {celsius} grados Celsius")
elif opcion == 18:
    reaumur = float(input("Ingrese la temperatura en grados Réaumur: "))
    fahrenheit = round((reaumur * 9 / 4) + 32, 2)
    print(f"{reaumur} grados Réaumur equivalen a {fahrenheit} grados Fahrenheit")
elif opcion == 19:
    reaumur = float(input("Ingrese la temperatura en grados Réaumur: "))
    kelvin = round((reaumur * 5 / 4) + 273.15, 2)
    print(f"{reaumur} grados Réaumur equivalen a {kelvin} grados Kelvin")
elif opcion == 20:
    reaumur = float(input("Ingrese la temperatura en grados Réaumur: "))
    rankine = round((reaumur * 9 / 4) + 491.67, 2)
    print(f"{reaumur} grados Réaumur equivalen a {rankine} grados Rankine")
else:
    print("Opción no válida")
