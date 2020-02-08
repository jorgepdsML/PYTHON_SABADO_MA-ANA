"""
archivo para leer los datos del archivo de texto
"""
import time
archivo=open("datos.txt","r")
temp,hum=[],[]
#acceder a cada linea del archivo de texto
for linea in archivo:
    #conseguir la cantidad de caracteres de cada linea
    N=len(linea)
    #tomar los primeros caracteres menos el ultimo caracter
    linea_n=linea[:N-1]
    print(linea_n)
    #separar los datos de temperatura y humedad
    datos=linea_n.split(sep=",")
    #agregar el dato de temperatura a la lista temp
    temp.append(float(datos[0]))
    #agregar el dato de humedad a la lista hum
    hum.append(float(datos[1]))
    time.sleep(1)
print(temp,sum(temp)/len(temp))
print(hum,sum(hum)/len(hum))
archivo.close()

