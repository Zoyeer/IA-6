#Mario Alberto Ponce Vazquez
#Registro: 20310317
#Materia: Inteligencia Artificial
#Curso de Python: Capitulo 23. El condicional if elif else e input, entrada de datos


#Ejercicio 40. Al siguiente código añadele un par de rangos de edad. 
#Uno de 18 años hasta 45 y otro de más de 100 años hasta 120.

edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad >= 1 and edad < 18:
	print('Eres menor de edad.')
elif edad >= 18 and edad <= 45:
    print('Eres mayor de edad, pero menor de 45')
elif edad >= 45 and edad < 100:
    print('Eres un adulto un poco viejo')
elif edad >= 100 and edad <= 120:
	print('Me sorprende que sigas vivo4.')
else:
	print('Edad no válida.')