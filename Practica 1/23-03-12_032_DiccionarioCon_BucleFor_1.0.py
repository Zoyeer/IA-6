#Mario Alberto Ponce Vazquez
#Registro: 20310317
#Materia: Inteligencia Artificial
#Curso de Python: Capitulo 32. Como usar diccionarios con el bucle for

#Ejercicio 49. Itera el diccionario teclado1 con un solo bucle for que muestre esto en la consola:

    
#Diccionario Teclado 1 con 3 categorias y cada categoria con un objeto en el
Teclado1 = {
    'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

#Iniciamos el bucle for para que corra por todas las categorias de Teclado1
for x in Teclado1:
    
    #Luego imprimimos tanto el valor de x que es la categorias como el objeto de la categoria en si y agregamos '=' y '.'
    print(x,"=", Teclado1[x] + ".")
