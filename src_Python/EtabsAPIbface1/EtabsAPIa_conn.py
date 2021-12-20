#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Conexion: Para usar esta script tiene que estar ejecutandose Etabs.

Methods.: 
    comtypes.client
        .GetActiveObject(Progit, interface=None, dynamic=False)
            .ApplicationExit(FileSave)

Progit      : es un cadena, str
interface   : objeto.
dynamic     : es un booleano, bool
"""
import sys
# import | importar la libreria requerida
import comtypes.client

# Definicion de variables para su uso
ETABSObject = None

try:
    # Connecting | coneccion
    ETABSObject = comtypes.client.GetActiveObject("CSI.ETABS.API.ETABSObject")
    print("Conexion exitosa!.Estableciendo a una instalcia exisistente")
except (OSError, comtypes.COMError):
    print("No se encontró ninguna instancia en ejecución del programa(Etabs).")
    sys.exit(-1)


# Close the program | Cerrar la aplicacion
print("La sesión actual de este programa se conectó haciendo uso de la API. \
Se recomenda que cierre este programa utilizando el programa desde el que se inició.")
input("Enter para cerrar Etabs!")
ETABSObject.ApplicationExit(False)

# clean up variables | limpiamos la variable y eliminamos
ETABSObject = None
del ETABSObject
sys.exit(-1)

# Show list of methods and properties | Muestra la lista de metodos y propiedades
# print(dir(ETABSObject))