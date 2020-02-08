
"""
este script es para realizar el registro de temperatura y humedad
por un determinado tiempo y cada 2 segundos
"""
#importar los modulos necesarios
import time
#crear un diccionario llamado registro
registro={"temperatura":[],"humedad":[]}
#tiempo de referencia
t1=time.time()
print("-------REGISTRANDO----")
while True:
    #control del tiempo de ejecución
    if (time.time()-t1)>=10:
        print("HA TRANSCURRIDO 10 SEGUNDOS")
        #cortar el bucle while
        break
    #rellenar datos en el diccionario por 2 segundos
    #temperatura
    registro["temperatura"].append(20)
    #humedad
    registro["humedad"].append(60)
    time.sleep(2)
print("---FIN DE REGISTRO---")
print("MOSTRAR LO QUE EL DICCIONARIO HA REGISTRADO")
#campo temperatura
#campo humedad
print("TEMPERATURA,HUMEDAD")
for temp,hum in zip(registro["temperatura"],registro["humedad"]):
    print(temp,hum)
