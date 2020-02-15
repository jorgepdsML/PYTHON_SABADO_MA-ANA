"""
Uso de clases para la manipulación de listas
"""
"""
[[1,2],
 [3,4]]
"""
class Matriz():
    def __init__(self,m1):
        #crear un atributo matriz1
        self.matriz1=m1
    def suma(self):
        #crear un variable local asociado al método suma
        m2=self.matriz1
        #recorriendo el número de filas
        val=0
        for x in m2:
            val=sum(x)+val
        return val
    def binarizacion(self,umbral):
        m1=self.matriz1
        #calculando el número de filas
        nf=len(m1)
        #calculando el número de columnas
        nc=len(m1[0])
        m2=[]
        for a in range(nf):
            m2.append([])
        #realizar el recorrido sobre cada fila y columna
        for x in range(nf):
            for y in range(nc):
                #condición
                if m1[x][y]>=umbral:
                    m2[x].append(255)
                else:
                    m2[x].append(0)
        return m2
#crear el objeto
a1=[[10,20,300],
    [30,400,404]]
o1=Matriz(a1)
print(o1.binarizacion(50))