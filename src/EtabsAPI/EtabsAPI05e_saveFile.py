#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Autor: F. JMucho. <fjmucho0@gmail.com>
Date: 
Description:
* Para usar esta script tiene que estar ejecutandose Etabs.

    cFile Methods/Metodos.: guardar archivo (modelo)
        ...
        .Save()     		'Saves the present model.
        ...
"""
import sys
import comtypes.client
# libreria para acceso a la plataforma y/o manejo de archvios
import os 

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

# 'initialize model | Inicializa nuevo modelo en blanco
resUnit = SapModel.InitializeNewModel()

# === FORMAS DE INICIALIZAR UN MODELO ===
# create new blank model | crea una nueva hoja en blanco
# resUnit = SapModel.File.NewBlank()
# create grid-only template model | Crea grilla
# resUnit = SapModel.File.NewGridOnly(4,12,12,4,4,24,24)
# create steel deck template model | 
resUnit = SapModel.File.NewSteelDeck(4,12.0,12.0,4,4,24.0,24.0)

# Unit Preferences | Preferencias de Unidad
N_mm_C = 6 # kN_mm_C
SapModel.SetPresentUnits(N_mm_C)

# get database units | Optener las unidades de la base de datos
dbUnits = None
dbUnits = SapModel.GetDatabaseUnits()
print(dbUnits) # vemos que solo contamos con una unidad asignada 'N_mm_C'


#full path to the model, set it to the desired path of your model
APIPath = 'C:\\CSi_ETABS_API_Example'
if not os.path.exists(APIPath):
    try:
        os.makedirs(APIPath) #| intenta crear un directorio.
    except OSError:
        print("Error: "+OSError) #| si no se tiene permiso laza un error.
ModelPath = APIPath + os.sep + 'exampleAPI_1-001.edb'
# ModelPath = APIPath + os.sep + 'exAPI_1-002.edb'
# 'save file  | guardar archivo
# System.IO.Directory.CreateDirectory("c:\CSI_API_temp")
# resUnit = SapModel.File.Save("C:\CSI_API_temp\example.edb")
resUnit = SapModel.File.Save(ModelPath)

# 'close ETABS | Cerrar aplicacion Etabs
ETABSObject.ApplicationExit(False)

# clean up variables | limpiamos las variables y eliminamos
del N_mm_C
ETABSObject, SapModel, retVersion, fullNameEtabs, resUnit = None, None, None, None, None
del ETABSObject, SapModel, retVersion, fullNameEtabs, resUnit
print("Su modelo de etabs se ha creado con exito, ")
sys.exit("Revise en su directorio C:\\CSi_ETABS_API_Example")