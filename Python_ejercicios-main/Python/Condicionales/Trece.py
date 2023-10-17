#Un reporte de salud muestra una tabla diferente del índice de masa corporal IMC de una persona que se calcula con la fórmula IMC=P/(E*E) en donde P es el peso en Kg. y E es la estatura en metros. Lea un valor de P y de E, calcule el IMC y muestre su estado según la siguiente tabla:

print("Ingrese los siguientes datos para comenzar a operar")
peso = float(input("Ingrese su peso en Kg: "))
talla = float(input("Ingrese su talla en metros: "))

total = peso / (talla * talla)

if total < 18.5:
    print(f"Su IMC es: {total} Desnutrido")
elif 18.5 <= total < 25:
    print(f"Su IMC es: {total} Normal")
elif 25 <= total < 30:
    print(f"Su IMC es: {total} Sobrepeso")
elif 30 <= total < 35:
    print(f"Su IMC es: {total} Obesidad Grado 1")
elif 35 <= total < 40:
    print(f"Su IMC es: {total} Obesidad Grado 2")
else:
    print(f"Su IMC es: {total} Obesidad Grado 3")
