print("Actividad #1")
print("Credito bancario")

nom=input("Ingrese su nombre:")
edad = int(input("Ingrese su edad:"))

if edad>=18:
    print("Puede acceder a un credito")
else:
    print("No puede acceder a un credito")

print("Actividad #2")
print("Costo de entrada")

cliente= input("Ingrese su nombre:")
edad= int(input("Ingrese su edad:"))

if edad<=4:
    print("Entrada gratis")
elif edad==5 and edad <=18:
    print("Paga 5 Euros")
else:
    print("Paga 18 Euros")

print("Actividad #3")
print("Calculadora operaciones basicas")

print("Realizaremos las operaciones")

num1= float(input("Ingrese el primer numero:"))
num2=float(input("Ingrese el segundo numero:"))
print("Operacion")
op=input("Ingrese la operacion deseada(Suma, Resta, Multiplicacion, Division):")
suma= num1+num2
resta= num1-num2
multiplicacion= num1*num2
division= num1/num2

if op == "suma":
    print("La suma es:", suma)
elif op== "resta":
    print("La resta es:",resta)
elif op== "multiplicacion":
    print("La multiplicacion es:",multiplicacion)
elif op== "division":
    print("La division es:",division)
else:
    print("No se reconoce la operacion")





