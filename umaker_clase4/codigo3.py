"""
definición de la función matmul(m1,m2)
"""
if __name__=="__main__":
    print("CODIGO EJECUTADO DIRECTAMENTE")
else:
    print("CODIGO IMPORTANDO POR OTRO ARCHIVO DE PYTHON")
    def matmul(m1, m2):
        # conseguir filas de ambas matrices
        Nf1, Nf2 = len(m1), len(m2)
        # conseguir columnas de la ambas matrices
        Nc1, Nc2 = len(m1[0]), len(m2[0])
        # identificar que ambas matrices tenga las mismas
        # dimensiones
        if Nf1 == Nf2 and Nc1 == Nc2:
            suma = 0
            # recorrer las filas
            for r in range(Nf2):
                # recorrer las columnas
                for c in range(Nc2):
                    suma += m1[r][c] * m2[r][c]
            return suma
        else:
            return None
    def linspace(v0, vf, N):
        razon = (vf - v0) / N
        # lista vacia
        l1 = list()  # []
        for val in range(N):
            l1.append(v0 + razon * val)
        return l1


    NAME = "ARCHIVO CODIGO3"





