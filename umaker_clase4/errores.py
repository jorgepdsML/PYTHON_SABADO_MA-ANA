"""
script para manejar errores en python
"""
import sys
try:
    a = float(input("INGRESAR VARIABLE 1: "))
    b = float(input("INGRESAR VARIABLE 2: "))
    c=a/b
    print("DIVISIÓN ES : ",c)
except ZeroDivisionError:
    print("DENOMINADOR FUE IGUAL A 0")
except ValueError:
    print("ERROR AL CONVERTIR DE STRING A FLOTANTE")
except:
    print("SOLO SE QUE SE GENERO UN ERROR EN EL BLOQUE TRY")

while True:
    try:
        a=float(input("INGRESE DATO1 "))
        b=float(input("INGRESE DATO2"))
        print(a/b)
    except:
        print("SIGA INTENTANDO")
