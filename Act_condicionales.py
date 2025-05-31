print("Generaciones digitales")
año=int(input("Ingrese su año de nacimiento:"))
if año>1920 and año<1945:
    print("Generacion Silenciosa")
elif año>=1946 and año<=1964:
    print("Generacion Baby boomer")
elif año>=1965 and año<=1979:
    print("Generacion X")
elif año>=1980 and año<=2000:
    print("Generacion Y")
elif año>=2000 and año<=2010:
    print("Generacion Z")
elif año>2010 and año<=2030:
    print("Nativos digitales")
else:
    print("Aun no existe un nombre asignado para esta generacion")