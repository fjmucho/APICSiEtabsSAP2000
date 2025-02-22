import inspect
import Myclass

print("--- Clases, objetos, y funciones de modulo ---")
# Buscamos las clases, objetos y funciones del modulo
for nombre, dato in inspect.getmembers(Myclass):
	# no mostramos los que inicien con __
	if nombre.startswith('__'):
		continue
	print(f"{nombre}, {dato}")

print("--- Buscamos las clases en el modulo ---\n")
for nombre, dato in inspect.getmembers(Myclass, inspect.isclass):
	print(f"{nombre}, {dato}")
exit()

# remplazar claseBase, claseHija por la clase a evaluar.
print("--- Buscamos las metodos en el modulo ---\n")
for nombre, dato in inspect.getmembers(Myclass.Constants, inspect.isfunction):
	print(f"{nombre}, {dato}")
print("------")
for nombre, dato in inspect.getmembers(Myclass.claseHija, inspect.isfunction):
	print(f"{nombre}, {dato}")

# optenemos la documentacion de la clase
print(Myclass.claseBase.__doc__)

# optenemos el codigo fuente de un metodo
print(inspect.getsource(Myclass.claseHija.miMetodo))

# optenemos la firma de la funcion que nos indica los parametros.
print(inspect.signature(Myclass.miMetodo))