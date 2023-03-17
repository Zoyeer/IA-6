#Mario Alberto Ponce Vazquez
#Registro: 20310317
#Materia: Inteligencia Artificial
#Curso de Python: Capitulo 33. Métodos con diccionarios


#Ejercicio 50. Elimina el diccionario teclado1 entero . De teclado2 elimina las claves 'Categoría' y 'Precio'. 
#Muestra la última clave ('Modelo') que queda en la consola.

#El diccionaro Teclado1
Teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

#El diccionaro Teclado2
Teclado2 = {
	'Categoria': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

#Eliminamos por completo el diccionario de Teclado1
del Teclado1

#Del diccionario Teclado 2 solo eliminamos la categoria y precio. Es importantes respetar letras mayusculas y acentos
del Teclado2['Categoria']
del Teclado2['Precio']      

#Finalmente imprimimos el valor del modelo que quedo en el diccionario Teclado2
print("El Modelo que queda es: " + Teclado2['Modelo'])