import pickle
l1=(10,20,[10,10])
print("DATO ORIGINAL",l1)
#CONVERTIR DE LISTA A FLUJO DE BYTES
b1=pickle.dumps(l1)
#crear objeto para guardar archivo binario
arch1=open("datos","wb")
#guardar archivo
arch1.write(b1)
#actualizar los cambios
arch1.close()
print("DATO EN FLUJO DE BYTES",type(b1),b1)
