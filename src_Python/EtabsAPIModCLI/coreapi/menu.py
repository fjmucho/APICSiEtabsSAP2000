#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 
# ************* 1 **********
EtabsAPI illustration: 0.0.1 
Autor: Francisco J.Mucho
Date: 25/03/21
Time: satrt 10:10am finish 12:00pm
# ************* 1 **********
"""
from collections import OrderedDict
import os, sys
# import EtabsAPIFile
from coreapi.EAPIFile import EtabsAPIcFile as efile

nombre='Etabs API'

# ************* 1 *************
def tipoStructura(op):
    """Elegir un tipo de plantilla/modelo""" 
    nombrets = "Menu estructura"
    cerrar = False
    menu_tipostruct = OrderedDict(
        [
            ('1', efile.nuevaHojaEnBanco),
            ('2', efile.nuevaHojaConGrilla),
            ('3', efile.nuevaHojaConPlanta),
            ('4', efile.cancelar),
            ('5', efile.cerrarAplicacion)
        ])
    # ************* 1.2 *************
    while not cerrar:
        print("="*len(nombrets))
        print(nombrets)
        print("="*len(nombrets))
        ubicacion = None
        for opcion, funcion in menu_tipostruct.items():
            ubicacion = funcion.__doc__
            print(f"[{opcion}] {funcion.__doc__}")
        opts = input(f"[{nombre}\\{nombrets}]> ")
        # Opciones de salir
        if opts == "4":
            bienvenidos()
            cerrar = True
        cerrar = opts=='5'
        # opciones de acceso
        funcionalidad = menu_tipostruct.get(opts, None)
        print(funcionalidad) # test
        # if funcionalidad:
            # efile.nuevaHojaEnBanco
    else: 
        print("Salir")
    return 0
def docs():
    '''Ver la documentacion'''
    # flata agreagr path, pero problema no del python si no del editor
    fileName = APIPath = "."+os.sep+'docs'+os.sep # os.path.pardir
    try:
        # print(fileName)
        docn = open(fileName+"leame.txt",'r')
        print(docn.read())
        input("continuar (Enter)")
        docn.close()
        bienvenidos()
    except (IOError, OSError):
        print(f"The file doesn't exist. {OSError}\n")
        cerrar()

def bienvenidos():
    menu_bienvenida = OrderedDict(
        [
            ('1', tipoStructura),
            ('2', docs),
            ('3', cerrar)
        ])
    priTitulo = f" Bienvenido a <{nombre}!> "
    # ************* 1.1 *************
    print("="*len(priTitulo))
    print(priTitulo)
    print("="*len(priTitulo))
    print(f"[1] {menu_bienvenida['1'].__doc__}")
    print(f"[2] {menu_bienvenida['2'].__doc__}")
    print(f"[3] {menu_bienvenida['3'].__doc__}")
    opcion = input(f"[{nombre}] (1)> ")
    if opcion == "1" or opcion=="": 
        tipoStructura(opcion)
    elif opcion == "2":
        print("As elegido primero ver la <documentacion>")
        docs()
    elif opcion == "3":
        print("As elegidos <salir> " '\r\nAs salido de la apliacion...')
        sys.exit(-1)
    else:
        mierror()
    return 0

def cerrar():
    '''salir de la aplicación'''
    print("ctrl+c, para salir o ecriba una letra diferente de 'si'.\n")
    opc = input("volver al menu(si) ")
    if opc == "" or opc.lower() == "si":
        bienvenidos()
    sys.exit(-1)
def mierror():
    print("La opción que has seleccionado, no esta implementado ...")
    opc = input("Volver an menu(si)> ")
    if opc == "" or opc.lower() == "si":
        bienvenidos()
    sys.exit(-1)