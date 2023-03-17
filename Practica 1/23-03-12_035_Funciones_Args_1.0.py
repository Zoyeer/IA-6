#Mario Alberto Ponce Vazquez
#Registro: 20310317
#Materia: Inteligencia Artificial
#Curso de Python: Capitulo 35. 

#Ejercicio 52. ¿Cuántos argumentos se utilizan en cada una de estas llamadas?

#Línea 4: cuatro argumentos
#Línea 5: tres argumentos
#Línea 6: un argumento
#Línea 7: dos argumentos

#Ejercicio 53. Completa el siguiente fragmento de código:

#Definimos la funcion y colocamos el *args como argumento
def colores(*args):
    
    #Imprimimos y utilizamos primero el segundo parametro y despues el primero
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

#Llamamos a la funcion y colocamos 2 parametros y solo usaremos 2 parametros en esta funcion
colores('rojo', 'azul')

#Ejercicio 54. Crea una función que realice la suma de cinco números utilizando solo *args. 
#Debes imprimir el resultado en la consola. La suma no se realizará directamente sobre el print().

#Definimos la funcion suma y ponemos como argumento *args
def suma(*args):
     
        #En la variable suma sumamaos todos los paramatros de la funcion
        suma = args[0] + args[1] + args[2] + args[3] + args[4]
        
        #Imprimimos el resultado de la funcion
        print("El resultado de la suma es:", suma)

#Llamamos a la funcion y le damos los 5 parametros con los que trabajara la funcion
suma(1,2,3,4,5)