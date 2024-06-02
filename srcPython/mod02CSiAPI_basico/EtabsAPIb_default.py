#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""Description:
    [evaluar si, esta instalado etabs: ...ejecutar otras acciones...
    caso contrario: lanzar un menzaje 'no tienes intalada etabs']->en evaluacion para incluir o no!, este algoritmo

    algoritmo de instrucciones:
        evaluar si, esta en ejecucion una instalcia de etabs
            adjuntar la instancia a la existente
        caso contrario:
            busco la ultima verion instalada e intentar conectarme 
            si coneccion es esitosa:
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
import os, sys, comtypes.client

try:
    ETABSObject = comtypes.client.GetActiveObject("CSI.ETABS.API.ETABSObject")
    print("Coneccion exitosa!.\nadjuntando a una instancia existente.")
except (OSError, comtypes.COMError):
    print("No se encontró ninguna instancia en ejecución del programa(Etabs).")

    print("Tratando de Ejecutar etabs!.")
    #create API helper object
    helper = comtypes.client.CreateObject('ETABSv1.Helper')
    helper = helper.QueryInterface(comtypes.gen.ETABSv1.cHelper)
    try: 
        #create an instance of the ETABS object from the latest installed ETABS
        ETABSObject = helper.CreateObjectProgID("CSI.ETABS.API.ETABSObject") 
        print("Coneccion esitosa!.")
    except (OSError, comtypes.COMError):
        print("Cannot start a new instance of the program.")
        sys.exit(-1)

    print("Ejecutando etabs!.")
    #start ETABS application | ejecutar la Aplicacion ETABS.
    ETABSObject.ApplicationStart()


#create SapModel object | crea instancia del objeto SapModel
smodel = ETABSObject.SapModel

# Unlocking model | Mantener Cerrado modelo (hace referencia al candadito de etabs)
# smodel.SetModelIsLocked(False)

# 'initialize model | Inicializa nuevo modelo en blanco
# resuts = smodel.InitializeNewModel()

# Close the program | Cerrar la aplicacion
input("Enter para cerrar Etabs!")
ETABSObject.ApplicationExit(False)

# clean up variables | limpiamos las variables y eliminamos
ETABSObject, smodel, resuts = None, None, None
del ETABSObject, smodel, resuts