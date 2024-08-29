"""Estudiante [Damian]: Contador de palabras
Escribir un programa que cuente el número de palabras
 en una oración ingresada por el usuario. 
 Debe incluir una función contar_palabras(oracion)
   que tome la oración como entrada y devuelva el número de palabras."""

def contar_palabras(oracion):
    lista_oracion=list(oracion)
    contador=0
    for x in lista_oracion:
        if x == " ":
            contador+=1
        
    print("la cantidad de palabras de la oracion son: ", (contador+1))

contar_palabras(input("ingrese la oracion:  \n"))
