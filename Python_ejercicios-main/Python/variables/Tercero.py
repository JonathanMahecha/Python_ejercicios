#Programa para calcular la distancia recorrida en un movimiento rectilíneo. Recuerde $x=v*t$ donde $v$ es velocidad y $t$ es tiempo. 
#Solicitar al usuario velocidad en kilómetros por hora (Km/h) y tiempo en horas (h) para obtener la distancia en kilómetros (Km).

kilometro_hora = int(input("Ingrese los kilometros por hora del viaje: "))
tiempo = int(input("Ingrese el tiempo en horas del viaje: "))
distancia = kilometro_hora*tiempo
print (f"La distancia en kilometros es:  {distancia}")

