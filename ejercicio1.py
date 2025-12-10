""""
https://colab.research.google.com/drive/11L8qDxtCPFtHwuSs1Mh8VE3hS4RUdbg6

Hola, mundo
Hacer un programa que pida el nombre y te salude por tu nombre

Restricciones
Mantener entrada, salida y concatenación separados

Escribir el programa sin usar variables
Escribir un programa que devuelva diferentes tipos de saludos a diferentes tipos de persona.

"""
def entrada():
    #entrada
    nombre = input("Ingresa el nombre: ")
    return nombre
def concatenacion(nombre):
    #concatenacion
    saludo = 'Hola ' + nombre
    return saludo
def salida(saludo):
    #salida
    print(saludo)

nom = entrada()
mensaje = concatenacion(nom)
salida(mensaje)

'''
nom = entrada()
mensaje = concatenacion(nom)
salida(mensaje)

'''
#Reto 1
print('Hola '+ input("Ingrese el nombre: "))

#Reto 2
personaLista = ["Jose", "Maria", "Ruth"]
saludoLista = ["Hola", "Hello", "Ciao"]
for i in range(3):
    print(saludoLista[i]+personaLista[i])