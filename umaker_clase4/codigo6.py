"""
#---------open()
archivo=open("datos.txt","a")
#método write
archivo.write(" PYTHON ")
#cerrar el recurso del archivo de texto
archivo.close()
"""
#---------leer el archivo de texto
archivo=open("datos.txt","r")
#imprimir cada linea del archivo de texto
for linea in archivo:
    print(type(linea),linea,len(linea))
archivo.close()
