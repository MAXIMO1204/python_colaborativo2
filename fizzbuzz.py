"""
Escribir un programa que imprima los números del 1 al 100. Pero para múltiplos de tres, 
imprimir "Fizz" en lugar del número y para los múltiplos de cinco, imprimir "Buzz". Para 
números que son múltiplos de tres y cinco, imprimir "FizzBuzz".
"""

for item in range (1,101):
    if (item % 3) == 0 and (item % 5)== 0:
        print("FizzBuzz")
    elif (item % 3) == 0:
        print("Fizz")
    elif (item % 5) == 0:
        print("Buzz")
    else:
        print (item)
    