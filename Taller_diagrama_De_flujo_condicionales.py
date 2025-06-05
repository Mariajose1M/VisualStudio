print("Taller de diagrama de flujo condicionales")

print("Actividad #1")
print("Indicar si un numero es positivo, negativo o cero")

num= int(input("Ingrese un numero (positivo, negativo o cero):"))
if num>0:
    print("El numero es positivo")
elif num<0:
    print("El numero es negativo")
else:
    print("El numero es igual a cero")

print("Actividad #2")
print("Calcular numero mayor")

nu1= int(input("Ingrese el primer numero:"))
nu2=int(input("Ingrese el segundo numero:"))
if nu1>nu2:
    print("El numero mayor es:", nu1)
elif nu1<nu2:
    print("El numero mayor es:", nu2)
else:
    print("Los numeros son iguales")

print("Actividad #3")
print("Indicar si un numero es par o impar")

nume= int(input("Ingrese un numero:"))
if nume/2==0:
    print("El numero es par")
else:
    print("El numero es impar")

print("Actividad 4")
print("Indicar si esta entre 10 y 20")

n= int(input("Ingrese un numero:"))
if n>10 and n<20:
    print("El numero esta entre 10 y 20")
else:
    print("El numero no esta entre 10 y 20")

print("Actividad 5")
print("Encontrar el numero mayor")

nu1= int(input("Ingrese el primer numero:"))
nu2= int(input("Ingrese el segundo numero:"))
nu3= int(input("Ingrese el tercer numero:"))
if nu1>nu2 and nu1>nu3:
    print("El numero mayor es:", nu1)
elif nu2>nu2 and nu2>nu3:
    print("El numero mayor es:", nu1)
else:
    print("El numero mayor es:", nu3)