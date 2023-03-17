#Mario Alberto Ponce Vazquez
#Registro: 20310317
#Materia: Inteligencia Artificial
#Curso de Python: Capitulo 27. El bucle while


#Ejercicio 42. Crea un bucle while que se ejecute hasta que x valga 15 con incrementos de 5.

x = 0

while x <= 15:
    print(x)
    x += 5

#Ejercicio 43. Crea un bucle while que se ejecute hasta que x valga -100 con decrementos de 20.

x = 0

while x >= -100:
    print(x)
    x -=20
    
#Ejercicio 44. Crea un bucle while que se ejecute hasta que x valga 0 con decrementos de 1 y que muestre 
#en cada ejecución esta frase con el valor de ejecución correspondiente: 'El valor del bucle es 10'...

x = 10

while x >= 0:
    print("El valor del bucle es ", x)
    x -=1