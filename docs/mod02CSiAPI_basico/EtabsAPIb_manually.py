#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""Description:
    algoritmo y/o instrucciones:

        evaluar si: esta en ejecucion una instalcia de etabs
            adjuntar la instancia a la existente
        caso contrario:
            evaluar si esta definido coneccion manual:
                ejecutar via ruta manual
            caso contrario:
                busco la ultima verion instalada e intentar conectarme 
                si coneccion es esitosa:
                lanzar mensage: coneccion exitosa
            ejecutar etabs

    Methods.:
        comtypes.client
            .GetActiveObject()
            .ApplicationStart()
            .CreateObject()
                .QueryInterface()
                .CreateObjectProgID()
            .ApplicationStart()
"""
import os, sys
import comtypes.client

# Variable para definir una instancia manual para Etabs.
rutaEspecifica = True

#if the above flag is set to True, specify the path to ETABS below
# si la bandera anterior se establece en True, entonces debe especificar la ruta a ETABS a continuación
ProgramPath = "C:\\Program Files\\Computers and Structures\\ETABS 19\\ETABS.exe"

#create API helper object
helper = comtypes.client.CreateObject('ETABSv1.Helper')
helper = helper.QueryInterface(comtypes.gen.ETABSv1.cHelper)
if rutaEspecifica:
    try:
        #'create an instance of the ETABS object from the specified path
        ETABSObject = helper.CreateObject(ProgramPath)
        print("Coneccion esitosa!.\nVia Coneccion Manual")
    except (OSError, comtypes.COMError):
        print("Cannot start a new instance of the program from " + ProgramPath)
        sys.exit(-1)

print("Ejecutando etabs!.")
#start ETABS application | ejecutar la Aplicacion ETABS.
ETABSObject.ApplicationStart()

#create SapModel object | crea instancia del objeto SapModel
smodel = ETABSObject.SapModel

# Unlocking model | Mantener Cerrado modelo (hace referencia al candadito de etabs)
# smodel.SetModelIsLocked(False)

# 'initialize model | Inicializa nuevo modelo en blanco
# resUnit = smodel.InitializeNewModel()

print("La sesión actual de este programa se conectó haciendo uso de la API. \
Se recomenda que cierre este programa utilizando el programa desde el que se inició.")
input("Enter para cerrar Etabs!")
# Close the program | Cerrar la aplicacion
ETABSObject.ApplicationExit(False)

# clean up variables | limpiamos las variables y eliminamos
ETABSObject, smodel, resUnit = None, None, None
del ETABSObject, smodel, resUnit