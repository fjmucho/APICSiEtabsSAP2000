#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import inspect
import comtypes.client as ctc

print("--- Clases, objetos, y funciones de modulo \n")
# Buscamos las clases, objetos y funciones del modulo
for nombre, dato in inspect.getmembers(ctc):
	# no mostramos los que inicien con __
	if nombre.startswith('__'):
		continue
	print(f"{nombre}, {dato}")

print("\n--- Buscamos las clases en el modulo \n")
for nombre, dato in inspect.getmembers(ctc, inspect.isclass):
	if nombre.startswith('__') or nombre.startswith('_'):
		continue
	print(f"{nombre}, {dato}")

# remplazar claseBase, ClaseHija(Constants) por la clase a evaluar.
print("\n--- Buscamos las metodos en el modulo/clase \n")
for nombre, dato in inspect.getmembers(ctc, inspect.isfunction):
	print(f"{nombre}, {dato}")
print("---metodos de la SubClase")
for nombre, dato in inspect.getmembers(ctc.Constants, inspect.isfunction):
	print(f"{nombre}, {dato}")


# optenemos la firma de la funcion que nos indica los parametros.
# print(inspect.signature(ctc.miMetodo))
print(inspect.signature(ctc.GetActiveObject))

# optenemos la documentacion de la clase
print("\n---Documentacion\n")
# print(ctc.clasebase__doc__)
print(ctc.__doc__)
# print(ctc.GetActiveObject.__doc__)

# optenemos el codigo fuente de un metodo
print("\n---Codigo fuente de la funcion ...\n")
print(inspect.getsource(ctc.GetActiveObject))
# print(inspect.getsource(ctc.claseHija.miMetodo))
exit()


# para todo lo anteriro se puede usar 
# print(help(nobrePackete))
# print(dir(nobrePackete))