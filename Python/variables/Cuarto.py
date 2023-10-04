#Programa que permita calcular la edad de una persona conociendo el año actual y el usuario digita su año de nacimiento.

año_nacimiento = int(input("Ingrese el año de nacimiento: "))
año_actual = int(input("Ingrese el año actual: "))
edad = año_nacimiento-año_actual
print(f"Usted tiene  {edad} de edad")

