#Mario Alberto Ponce Vazquez
#Registro: 20310317
#Materia: Inteligencia Artificial
#Curso de Python: Capitulo 31. ¿Qué son los diccionarios de Python?


#Ejercicio 48. Del diccionario teclado2 del capítulo, muestra los elementos Modelo y Precio con 
#presentación en un print(). El resultado será esto en la consola:

#Se declara el diccionario teclado1 que va encerrado entre llaves y que tiene 3 categorias: categoria, modelo y precio.
#Utilizamos comillas simples para guardar las categorias y sus elementos y ademas utilizamos dos puntos para separar la categoria del objeto
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

#Se declara el diccionario teclado2 con las mismas categorias que el diccionario anterior
teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

#Se manda a imprimir lo que contiene tanto el modelo como el precio del diccionario del teclado 2
print("El modelo ", teclado2['Modelo'], "cuesta", teclado2['Precio'])
