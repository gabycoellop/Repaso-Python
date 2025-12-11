#while se repite el bloque de codigo mientras la condicion sea verdadera(True)
"""
seguir = True

while seguir:
    print('hola')

    fin = input("Desea seguir con este while? s/n")
    if fin == "n":
        seguir = False
        print("Esto se ha acabado")
"""
#while con else
"""
nombre = "Maria"
while nombre == "Maria":
    print("Hola, nombre")
else:
    print("No es Maria")
"""

#Imprimir valores del 1 al 100
cont = 0
while cont < 100:
    cont = cont + 1
    print(cont)

#realizar un programa que muestre la tabla de multiplicar dado un numero

def tablaDeMultiplicar(numero):
    numero = int(numero)
    for i in range(1,11):
        print(f"{numero}x{i}={numero*i}")

num = input("Introduce un numero: ")
tablaDeMultiplicar(num)

