import pickle
#crear objeto para leer el contenido de datos
a1=open("datos","rb")
#método read para leer todo el contenido en bytes
dato=a1.read()
#convertir de flujo de bytes al tipo de dato original
orig=pickle.loads(dato)
a1.close()
print("EL DATO FUE:",orig)