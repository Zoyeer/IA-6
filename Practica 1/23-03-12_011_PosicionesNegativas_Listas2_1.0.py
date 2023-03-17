#Mario Alberto Ponce Vazquez
#Registro: 20310317
#Materia: Inteligencia Artificial
#Curso de Python: Capitulo 11. Posiciones negativas - Listas 2


#Ejercicio 26. Utiliza las posiciones negativas para acceder e imprimir algunos de los colores de esta lista. 
#Los colores a los que tienes que acceder son 'naranja', 'amarillo', 'lila', 'blanco' y 'rojo'.

Colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

#Naranja
UltimoColor = Colores[-1]
print(UltimoColor)

#Amarillo
PenultimoColor = Colores[-7]
print(PenultimoColor)

#Lila, blanco y rojo
print(Colores[-5], "\n" + Colores[-2], "\n" + Colores[-10])