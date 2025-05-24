num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
#la operacion de la division
divi = num1 // num2 
print(f"la division de los dos numeros es: ", divi)

print("_____________________________________________\n")
print("pontencia")
base = int(input("ingrese la base:"))
base1 = int(input("ingrese la segunda base: "))
exp = int(input("ingrese la potencia: "))
exp1 = int(input("ingrese la segunda potencia "))
print("el resultado de la base 1 es: ", base ** exp)
print("el resultado de la base 2 es: ", base1 ** exp1)

print("______________________________________________\n")
print("entre parentesis y potencias")
x = int(input("ingrese el primer numero "))
y = int(input("ingrese el segundo numero "))
exponente = int(input("ingrese la potencia "))
result = (x * y) ** exponente
print(f"el resultado es: ", result)