"""
SCRIPT PARA EL DESARROLLO DE ESTRUCTURA DE DATOS
"""
l1=[]
for a in range(10):
    l1.append(a)
#lista 2
l2=[[1,2] for a in range(2)]
print("LISTA 1 ES :{}".format(l1))
print("LISTA 2 ES :{}".format(l2))
#DEFINIR UNA MATRIZ DE 2x2
M1=[[1,2],
    [3,1]]
#RECORRIDO SOBRE LA MATRIZ M1
#determinar filas de la lista M1
Nf=len(M1)
#determinar columnas de la columna M1
Nc=len(M1[0])
#calcular la formula
#var=a+b+c+d
suma=0
for r in range(Nf):
    for c in range(Nc):
        suma+=M1[r][c]
print("LA SUMA ES :{}".format(suma))


