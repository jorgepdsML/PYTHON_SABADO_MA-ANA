class rectangulo():
    var=200
    #definir método area
    def area(self,a,b):
        #definir atributo base , altura
        self.base=a
        self.altura=b
        print("AREA ES: ",a*b)
    def perimetro(self):
        print("PERIMETRO ES: ",2*(self.base+self.altura))
#instanciar un objeto
r1=rectangulo()
#invocar al método area
r1.area(5,2)
#invocar al método perimetro
r1.perimetro()