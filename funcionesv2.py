print("mas sobre funciones")
# aqui se escriben las funciones
def suma_ab(a,b):
    s=a+b
    return s
def resta_ab(a1,b1):
    r=a1-b1
    return r
def div_ab(a2,b2):
    d=a2/b2
    return d
def mul_ab(a3,b3):
    m=a3*b3
    return m
# llamadas a funcion
n1=int(input("ingresa el primer numero: "))
n2=int(input("ingresa el segundo numero: "))
suma=suma_ab(n1, n2)
print("Calculando suma")
print(f"la suma de {n1} y {n2} es: {suma}")
#--RESTA--
num=int(input("ingresa el primer numero: "))
num=int(input("ingresa el segundo numero: "))
print("calculando resta")
resta=resta_ab(num, num)
print(f"la resta de {num} y {num} es: {resta}")
#--MULTIPLICACION--
nu1=int(input("ingresa el primer numero: "))
nu2=int(input("ingresa el segundo numero: "))
print("calculando multiplicacion")
multiplicacion=mul_ab(nu1, nu2)
print(f"la multiplicacion de {nu1} y {nu2} es: {multiplicacion}")
#--DIVISION--
num1=float(input("ingresa el primer numero: "))
num2=float(input("ingresa el segundo numero: "))
print("Calculando division")
division=div_ab(num1,num2)
print(f"la division de {num1} y {num2} es: {division}")
