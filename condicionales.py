edad= int(input("Introduce tu edad:"))
if edad>=18: 
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print("Uso de AND")
a= 25
b= 50
if a>b and b<a:
    print("Ambas condiciones son verdaderas")

print("Multiples if")
x=25
if x>10:
    print("por encima de diez")
    if 2>20:
        print(" y tambien por encima de veinte")
    else:
        print("pero no por encima de veinte")

print("Sentencia ELIF")
n1= int(input("Ingrese el primer numero"))
n2= int(input("Ingrese el segundo numero")) 
mt=n1*n2
if mt>100 and mt>150:
    print("El resultado de la operacion es mayor a 100 y menor a 150")
elif mt==100:
    print("El resultado de la operacion es igual a 100")
elif mt<100:
    print("El resultado de la operacion es menor a 100")
else:
    print("El resultado es mayor a 150")



