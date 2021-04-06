#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Para usar esta script tiene que estar ejecutandose Etabs.
Metodos - cFile Methods
    ...
    .NewBlank()        'Creates a new, blank model.
    .NewGridOnly()     'Creates a new grid-only model from template.
    .NewSteelDeck()    'Creates a new steel deck model from template.
    .OpenFile()        'Opens an existing file.
    .Save()            'Saves the present model.
    
"""
import os, sys
import comtypes.client

#attach to a running instance of ETABS|... - Connecting | coneccion
try:
    #get the active ETABS object |optener ... 
    ETABSObject = comtypes.client.GetActiveObject("CSI.ETABS.API.ETABSObject")
    print("Coneccion exitosa!.\nadjuntando a una instancia existente.")
except (OSError, comtypes.COMError):
    # No running instance of the program found or failed to attach.
    print("No se encontró ninguna instancia en ejecución del programa(Etabs).")
    sys.exit(-1)
# create SapModel object | Crea el objeto Modelo
SapModel = ETABSObject.SapModel
# Unlocking model | Mantener Cerrado modelo (hace referencia al candadito de etabs)
SapModel.SetModelIsLocked(False)

# initialize model | Inicializa nuevo modelo en blanco
resUnit = SapModel.InitializeNewModel()


# create grid-only template model | Crea grilla
resUnit = SapModel.File.NewGridOnly(4,12,12,4,4,24,24)
# hacer pruebas (test), por presentar error en ocaciones, ...

# Unit Preferences | Preferencias de Unidad
N_mm_C = 6 # kN_mm_C
SapModel.SetPresentUnits(N_mm_C)

# get database units | Optener las unidades de la base de datos
dbUnits = None
dbUnits = SapModel.GetDatabaseUnits()
print(dbUnits) # vemos que solo contamos con una unidad asignada 'N_mm_C'

# clean up variables | limpiamos las variables y eliminamos
del N_mm_C
ETABSObject, SapModel, retVersion, fullNameEtabs, resUnit = None, None, None, None, None
del ETABSObject, SapModel, retVersion, fullNameEtabs, resUnit
sys.exit()