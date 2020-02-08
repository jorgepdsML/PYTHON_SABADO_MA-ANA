def sumar(a,b):
    print(a+b)
sumar(10,20)
#copiar el comportamiento de la función sumar
jorge=sumar
jorge(1000,2000)

def func2():
    val=200
    def func1():
        print("FUNCION1")
    func1()
    print("FUNCION2 FINALIZADA")
func2()



#-----definir una función llamada polinomio
def polinomio(a0,a1,a2):
    def calculo(x):
        val=a0*(x**2)+a1*x+a2
        return val
    #retornar una copia de la función
    return calculo
p=polinomio(1,1,1)
suma=0
for val in range(-3,4,1):
    suma=suma+p(val)
print("LA SUMA DEL POLINOMIO ES: {}".format(suma))