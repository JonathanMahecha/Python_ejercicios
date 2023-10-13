#Solicitar al usuario una distancia en metros y transformar a km., cm. o mm. 
metros = float(input("Ingresa la distancia en metros: "))

kilometros = metros / 1000
centimetros = metros * 100
milimetros = metros * 1000

print(f"{metros} metros son equivalentes a:")
print(f"{kilometros} kilómetros")
print(f"{centimetros} centímetros")
print(f"{milimetros} milímetros")
