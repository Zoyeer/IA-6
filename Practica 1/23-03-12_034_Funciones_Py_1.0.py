#Mario Alberto Ponce Vazquez
#Registro: 20310317
#Materia: Inteligencia Artificial
#Curso de Python: Capitulo 34. Como crear y llamar funciones en Python 

#Ejercicio 50. Crea una función que realice una suma. 
#Para ello, tendrás que añadir dos argumentos (numero1 y numero2). 
#En su interior, especificarás un print() que muestre el resultado de la suma. 
#Deberás hacer tres llamadas que como resultado de la suma den los valores 30, 50 y 57000. 
#Los números que introduzcas en la llamada pueden ser los que quieras siempre que coincidan los resultados en el print().

#Definimos la funcion sumar con dos parametros los cuales deben ser 2 numeros enteros
def sumar(num1, num2):
    
    #En la variable suma tomamos los dos parametros de la funcion y los sumamos
    suma = num1 + num2
    
    #Imprimimos el resultado de la suma
    print("El resultado de la suma es:", suma)
    
#Mandamos a llamar 3 veces a la misma funcion y le damos diferentes parametros para que nos den los valores esperados
sumar(10,20)
sumar(30,20)
sumar(50000,7000)
