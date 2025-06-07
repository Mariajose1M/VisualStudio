print("Taller de diagrama de flujo condicionales")

#------------------------------------------------------------------------------------

print("Actividad #1")
print("Indicar si un numero es positivo, negativo o cero")

num= int(input("Ingrese un numero (positivo, negativo o cero):"))
if num>0:
    print("El numero es positivo")
elif num<0:
    print("El numero es negativo")
else:
    print("El numero es igual a cero")

#------------------------------------------------------------------------------------

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

#------------------------------------------------------------------------------------    

print("Actividad #3")
print("Indicar si un numero es par o impar")

nume= int(input("Ingrese un numero:"))
if nume%2==0:
    print("El numero es par")
else:
    print("El numero es impar")

#------------------------------------------------------------------------------------    

print("Actividad 4")
print("Indicar si esta entre 10 y 20")

n= int(input("Ingrese un numero:"))
if n>10 and n<20:
    print("El numero esta entre 10 y 20")
elif n==10:
    print("El numero es igual a 10")
elif n==20:
    print("El numero es igual a 20")
else:
    print("El numero no esta entre 10 y 20")

#------------------------------------------------------------------------------------    

print("Actividad 5")
print("Encontrar el numero mayor")

nu1= int(input("Ingrese el primer numero:"))
nu2= int(input("Ingrese el segundo numero:"))
nu3= int(input("Ingrese el tercer numero:"))
if nu1>nu2 and nu1>nu3:
    print("El numero mayor es:", nu1)
elif nu2>nu1 and nu2>nu3:
    print("El numero mayor es:", nu2)
else:
    print("El numero mayor es:", nu3)

#------------------------------------------------------------------------------------

print("Actividad 6")
print("calculo precio final y descuento")

pf= float(input("Ingrese el precio final del producto:"))
if pf>100:
    des=10*pf/100
    print("Se realiza un descuento del 10%, el precio final actual de su producto es:",pf-des)
else:
    print("El precio final no es apto para el descuento, el precio final es:",pf)

#------------------------------------------------------------------------------------

print("Actividad 7")
print("Verificacion si puede votar")

edad=int(input("Ingrese su edad:"))
if edad>=18:
    print("Usted es mayor de edad, puede votar")
else:
    print("Usted es menor de edad,  no puede votar")

#------------------------------------------------------------------------------------

print("Actividad 8")
print("Descuento a  clientes VIP")

vip= input("¿Usted es cliente VIP?(si o no):")
precio= float(input("Ingrese el precio"))
if vip=="si":
    des=20*precio/100
    print("El precio final con descuento es:", precio-des)
else:
    print("Por ser cliente normal, no tiene descuento")

#------------------------------------------------------------------------------------

print("Actividad 9")
print("Determinar si el  numero es multiplo de 3 y 5")

nu=int(input("Ingrese un numero:"))
if nu%3==0 and nu%5==0:
    print("El numero es multiplo de 3 y 5 al  mismo tiempo")
elif nu%3==0:
    print("El numero solo es multiplo de 3")
elif nu%5==0:
    print("El numero solo es multiplo de 5")
else:
    print("El numero no es multiplo ni de 3 ni de 5")

#------------------------------------------------------------------------------------

print("Actividad 10")
print("Determinar si el numero es divisible entre otros")

n1= int(input("Ingrese el numero para verificar  si es divisible:"))
n2= int(input("Ingrese el primer numero  para verificar si es divisor:"))
n3= int(input("Ingrese el segundo numero para verificar si es divisor:"))
if n1%n2==0 and n1//n3==0:
    print("El numero es divisible por los dos numeros")
elif n1%n2==0:
    print ("El  numero solo es divisible por:",n2)
elif n1%n3==0:
    print("El numero solo es divisible por:",n3)
else:
    print("El numero no es divisible por ninguno de los dos numeros")

#------------------------------------------------------------------------------------   

print("Actividad 11")
print("Determinar si el terccer numero  de la lista es mayor a 10")

lista= []
lista.append (int(input("Ingrese el primer numero:")))
lista.append (int(input("Ingrese el segundo numero:")))
lista.append (int(input("Ingrese el tercer numero:")))
lista.append (int(input("Ingrese el cuarto numero:")))
lista.append (int(input("Ingrese el quinto numero:")))
print("Lista con los numeros ingresados:", lista)
if lista[2]>10:
    print("Mayor a 10")
else:
    print("Menor o igual a 10")

#------------------------------------------------------------------------------------

print("Actividad 12")
print("Determinar si el 7 esta en la lista")
lista= [3,5,7,9]
num= int(input("Ingrese un numero:"))
if 7 in lista:
    print("Esta en la lista")
else:
    print("No esta en la lista")

#------------------------------------------------------------------------------------

print("Actividad 13")
print("Suma de los elementos de la lista")

lista= [4,6,2,8]
if lista[0] + lista[1] >10:
    print("Suma alta")
else:
    print("Suma baja")

#------------------------------------------------------------------------------------

print("Actividad 14")
print("verificar si el nombre de la lista es correcto")

lista= ["Ana", "Luis", "Pedro", "Marta"]
nombre= input("Ingrese un nombre:")
if lista[3]=="Marta":
    print("Nombre correcto")
else:
    print("Nombre incorrecto")

#------------------------------------------------------------------------------------

print("Actividad 15")
print("Cambiar el color")

lista= []
lista.append (input("Ingrese el primer color:"))
lista.append (input("Ingrese el segundo color:"))
lista.append (input("Ingrese el tercer color:"))
print(f"Lista de coloreres: {lista}")
if lista[1]=="Azul":
    lista[1]="Rosado"
    print("Lista actualizada:",lista)
else:
    print("El color no es Azul, por lo tanto la lista continua igual")

#------------------------------------------------------------------------------------

print("Actividad 16")
print("Orden de la tupla")

tupla=(5,8,12,20)
if tupla[0]<tupla[-1]:
    print("Orden ascvendente")
else:
    print("Orden descendente")

#------------------------------------------------------------------------------------

print("Actividad 17")
print("Determina si el valor es mayorn a 30")

tupla=(25,32,28)
if tupla[1]>30:
    print("Edad mayor a 30")
else:
    print("Edad menor a 30")

#------------------------------------------------------------------------------------

print("Actividad 18")
print("Cambiarle el segundo valor a la tupla")
tupla= (1,2,3)
lista= list(tupla)
if lista[1]==2:
    lista[1]=10
    print(lista)
    tuplaa= tuple(lista)
    print("La tupla ha sido actualizada:", tuplaa)
else:
    print("El segundo valor no cambia, la tupla continua igual")

#------------------------------------------------------------------------------------

print("Actividad 19")
print("Cambiar el segundo valor")

tupla= (4,9)
if tupla[1]>5:
    print("Coordenadas altas")
else:
    print("Coordenadas bajas")

#------------------------------------------------------------------------------------

print("Actividad 20")
print("Compara si las tuplas son iguales")

tupla1= (3,4)
tupla2= (3,5)
if tupla1==tupla2:
    print("Tuplas iguales")
else:
    print("Tuplas diferentes")

#------------------------------------------------------------------------------------

print("Actividad 21")
print("Verificar la edad en un diccionario")

diccionario={"nombre":"Juan","edad":17}
if diccionario["edad"]>=18:
    print("Adulto")
else:
    print("Menor de edad")

#------------------------------------------------------------------------------------

print("Actividad 22")
print("Cambiar el valor de edad en el diccionario")
diccionario={"nombre":"Lucia","edad":20}
if diccionario["edad"]>18:
    diccionario["edad"]=21
    print("Se ha actualizado la edad:", diccionario)
else:
    print("La edad no es mayor a 18, por lo tanto no se actualiza")

#------------------------------------------------------------------------------------

print("Actividad 23")
print("Agregar clave al diccionario")

diccionario={"nombre":"Carlos"}
if "ciudad" in diccionario:
    print("La clave ciudad ya existe:", diccionario)
elif "ciudad" not in diccionario:
    diccionario["ciudad"]="Bogota"
    print("Se ha agregado la clave ciudad:", diccionario)
else:
    print("La clave ciudad no se ha agregado:", diccionario)

#------------------------------------------------------------------------------------

print("Actividad 24")
print("Verificar si la clave ya existe")

diccionario={"producto": "pan", "precio": 1200}
if "precio" in diccionario:
    print("El precio es:", diccionario["precio"])
else:
    print("No hay precio")

#------------------------------------------------------------------------------------

print("Actividad  25")
print("Indicar si una clave hace parte de el diccionario y su precio")

diccionario={"pan":1200,"leche": 2000}
if "pan" in diccionario:
    print("El precio del pan es:",diccionario["pan"])
else:
    print("Productto no disponible")

#------------------------------------------------------------------------------------


