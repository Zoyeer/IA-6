#Mario Alberto Ponce Vazquez
#Registro: 20310317
#Materia: Inteligencia Artificial
#Curso de Python: Capitulo 24. Comprobar datos en listas y tuplas


#Ejercicio 41. Haz una tupla que contenga cuatro colores de tu elección. 
#Tendrás que poner una condición con el condicional if para cada color que le avise al usuario 
#que el color está en la tupla con un mensaje como este: print('El color rojo está admitido') y 
#una condición False para contemplar cualquier color que no esté en la tupla con un mensaje 
#como este: print('Color no admitido'). No puedes utilizar el operador ==. Además tendrás que hacer esto con un 
#input() que permita introducir un color al usuario.

Tupla = ('rojo', 'azul', 'negro', 'morado')

Color = input("Ingrese un color: ")

if Color in Tupla:
    print("El color", Color, "esta admitido")
    
else:
    print("El color", Color, "no esta admitido")