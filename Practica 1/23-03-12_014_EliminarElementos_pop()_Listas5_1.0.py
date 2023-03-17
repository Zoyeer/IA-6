#Mario Alberto Ponce Vazquez
#Registro: 20310317
#Materia: Inteligencia Artificial
#Curso de Python: Capitulo 14. Eliminar elementos con pop() - Listas 5


#Ejercicio 29. Elimina de la siguiente lista los elementos 'azul' y 'blanco'. 
#Solo puedes eliminarlos utilizando el método pop(). 
#Además, tendrás que guardar esos dos colores en una nueva lista.

Colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

Eliminado1 = Colores.pop(1)
Eliminado2 = Colores.pop(-2)

print("\nLos colores eliminados son: ", Eliminado1, "y", Eliminado2)

Colores2 = ['purpura', 'violeta', Eliminado1, Eliminado2]
print("\nLa nueva lista es con los colores eliminados es ", Colores2)
