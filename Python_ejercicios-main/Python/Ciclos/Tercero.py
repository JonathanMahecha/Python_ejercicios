#Escriba un programa para mostrar n términos de número natural y su suma (Fibonacci).

n = 10
suma = 0

print(f"Los {n} números de la serie de Fibonacci son:")

form1 = 0
form2 = 1
print(form1, form2, end=" ")
for i in range(3, n + 1):
    form3 = form1 + form2
    print(form3, end=" ")
    form1, form2 = form2, form3

for i in range(1, n + 1):
    suma += i

print(f"\nLa suma de los {n} términos es: {suma}")
