"""
ESTE SCRIPT IMPORTARA EL MODULO codigo3.py
"""
# importar modulo llamado codigo3
import codigo3 as cod3
import sys
ruta=sys.path
print(ruta)
ruta.append("C:\\Users\\pdsjo\\Desktop\\modulo_python")
import soymodulo
# utilizar linspace(vo,vf,N)
l1 = cod3.linspace(10, 20, 20)
l2 = cod3.linspace(0, 10, 11)
