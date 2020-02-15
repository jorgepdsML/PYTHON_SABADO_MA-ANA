class persona():
    #método __init__
    def __init__(self,n,a):
        # creando o definiendo atributo
        self.apellido=a
        self.nombre=n
        print("OBJETO CREADO :",self.nombre,self.apellido)
    def caminar(self):
        print("YO PUEDO CAMINAR")
    def hablar(self):
        print("YO PUEDO HABLAR",self.nombre)
#INSTANCIAR UN OBJETO
o1=persona("JORGE","MIRANDA")
#acceder al atributo nombre delobjeto o1
name=o1.nombre
print("EL NOMBRE ES : ",name)
