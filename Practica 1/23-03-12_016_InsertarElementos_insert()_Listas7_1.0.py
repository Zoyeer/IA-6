#Mario Alberto Ponce Vazquez
#Registro: 20310317
#Materia: Inteligencia Artificial
#Curso de Python: Capitulo 16. Insertar elementos con insert() - Listas 7

#Ejercicio 31. Añade a la siguiente lista los colores 'magenta' y 'turquesa' utilizando insert(). 
#Tendrás que posicionar 'magenta' en la posición siguiente a la de 'lila' y 'turquesa' en la penúltima posición. 
#Deberás hacer esto utilizando posiciones de lista negativas.

Colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

Colores.insert(-4,'magenta')
Colores.insert(-1,'turquesa')

print(Colores)