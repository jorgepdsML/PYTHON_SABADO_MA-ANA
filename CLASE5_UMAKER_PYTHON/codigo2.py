class persona():
    def mostrar_nombre(self,n):
        #crear atributo minombre
        self.minombre=n
        print("MI NOMBRE ES : ",n)
#creando una instancia de la clase persona
o1=persona()
nombre=input("INGRESAR ARGUMENTO NOMBRE")
#acceder al método mostrar_nombre
o1.mostrar_nombre(nombre)
#acceder al atributo minombre
n1=o1.minombre
print(n1)
