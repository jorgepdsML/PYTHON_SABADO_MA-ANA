#importar un modulo
from tkinter import *
#CREAR UN OBJETO
api=Tk()
#geometry
api.geometry("500x500")
#definitir titulo del interfaz
api.title("INTERFAZ GRAFICA EN TKINTER")
#CREAR UN OBJETO DE LA CLASE Button
def encender():
    print("BOTON PRESIONADO , ENCENDIDO")
def apagar():
    print("BOTON PRESIONADO , APAGADO")
boton1=Button(api,text="BOTON DE ENCENDER",command=encender,fg="red")
boton2=Button(api,text="APAGAR",command=apagar,fg="blue")
boton1.place(x=0,y=0)
boton2.place(x=150,y=0)
#mainloop
api.mainloop()
print("FINISH")