#Solicitar notas de 0.0 a 5.0 a un estudiante y calcular promedio.  
#Mostrar como "Aprobó" si el promedio es mayor o igual a 3.0, o mostrar 
#"No aprobó" si su nota es menor a 3.0. 

print("Ingrese sus 5 notas para calcular su promedio")

numero1 = float(input("Escriba el primer número: "))
numero2 = float(input("Escriba el segundo número: "))
numero3 = float(input("Escriba el tercer número: "))
numero4 = float(input("Escriba el cuarto número: "))
numero5 = float(input("Escriba el quinto número: "))

resultado = (numero1 + numero2 + numero3 + numero4 + numero5) / 5

if resultado >= 3.0:
    print(f"Su resultado es {resultado}. Aprobó")
elif resultado < 3.0:
    print(f"Su resultado es {resultado}. No aprobó")
