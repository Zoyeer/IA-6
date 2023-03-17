#Mario Alberto Ponce Vazquez
#Registro: 20310317
#Materia: Inteligencia Artificial
#Curso de Python: Capitulo 12. Eliminar elementos con del() - Listas 3

#Ejercicio 27. De esta lista, elimina los colores 'azul', 'marrón', 'negro' y 'rosa'. 
#Debes utilizar al menos una vez las posiciones negativas para eliminar un color. 
#Después, imprime la lista para ver los colores que se han eliminado.

Colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

#Eliminando colores
del Colores[1]
del Colores[4]
del Colores[-4]
del Colores[-3]


print(Colores)
