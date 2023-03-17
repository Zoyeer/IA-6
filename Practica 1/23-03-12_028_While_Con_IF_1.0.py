#Mario Alberto Ponce Vazquez
#Registro: 20310317
#Materia: Inteligencia Artificial
#Curso de Python: Capitulo 28. El bucle while con condicional if


#Ejercicio 45. Crea un bucle while con las siguientes características:
#El valor inicial de la variable x será de 0.
#El valor de incremento será 1.
#La condición de salida del bucle será menor o igual a 30.
#La ejecución se deberá romper cuando x valga 15.
#Debes imprimir la siguiente frase cada vez que se ejecute el bucle: 'El valor del bucle es: ' + x.
#Debes saltarte las ejecuciones con valor de x en 4, 6 y 10.
#En cada salto de ejecución, deberás mostrar los valores saltado con este mensaje: 'Se saltó el valor ' + x ' de x'.
#Cuando se rompa la ejecución del bucle deberás mostrar un mensaje indicándolo: 
#'Se rompió la ejecución del bucle cuando x valía ' + x.

#Se inicializa la variable en 0
x = 0

#El bucle funcionara mientras x sea menor o igual a 30
while x <= 30:
    
    #Comenzamos a contar de 1 en 1
    x += 1
    
    #Si el numero es igual a 4, 6 o 7 entonces se imprimira que se salto ese numero
    if x == 4 or x == 6 or x == 7:
        print("Se salto el valor ", x)
        
    #Si se cumple la condicion anterior se salta la indicacion de imprimir en que numero va el bucle
        continue
    
    #Cuando x llegue a 15 entonces se rompera el bucle y se imprimira que la ejecucion del bucle se detuvo
    if x == 15:
        print ("Se rompio la ejecucion del bucle cuando x valia: ", x)
        break
    
    #Mientras que no se cumpla ninguno de los condicionales anteriores, el contador seguira y se imprimira su valor
    print("El valor del bucle es ", x)
    
    
    
        