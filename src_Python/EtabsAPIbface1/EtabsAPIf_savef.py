#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Description save: Para usar esta script tiene que estar ejecutandose Etabs.

    cFile Methods/Metodos.: guardar archivo (modelo)
        ...
        .Save()     		'Saves the present model.
        ...
"""
import sys
import comtypes.client
# libreria para acceso a la plataforma y/o manejo de archvios
import os

try:
    ETABSObject = comtypes.client.GetActiveObject("CSI.ETABS.API.ETABSObject")
    print("Coneccion exitosa!.\nadjuntando a una instancia existente.")
except (OSError, comtypes.COMError):
    print("No se encontró ninguna instancia en ejecución del programa(Etabs).")
    sys.exit(-1)
# create SapModel object | Crea el objeto Modelo
smodel = ETABSObject.SapModel
# Unlocking model | Mantener Cerrado modelo (hace referencia al candadito de etabs)
smodel.SetModelIsLocked(False)
# 'initialize model | Inicializa nuevo modelo en blanco
resUnit = smodel.InitializeNewModel()
# create steel deck template model | 
resUnit = smodel.File.NewSteelDeck(4,12.0,12.0,4,4,24.0,24.0)

# Unit Preferences | Preferencias de Unidad
N_mm_C = 6 # kN_mm_C
smodel.SetPresentUnits(N_mm_C)
print(smodel.GetPresentUnits())
# get database units | Optener las unidades de la base de datos
dbUnits = None
dbUnits = smodel.GetDatabaseUnits()
print(dbUnits) # vemos que solo contamos con una unidad asignada 'N_mm_C'

# 'set project information data
ret = smodel.SetProjectInfo("Ecobise E.I.R.L", "Computers and Structures, Inc.")
ret = smodel.SetProjectInfo("Project Name TestEtabsAPI", "API Testing")
ret = smodel.SetProjectInfo("My Item", "My Data")

#full path to the model, set it to the desired path of your model
APIPath = 'C:\\CSi_ETABS_API_Example'
if not os.path.exists(APIPath):
    try: os.makedirs(APIPath) #| intenta crear un directorio.
    except OSError: print("Error: "+OSError) #| si no se tiene permiso laza un error.
ModelPath = APIPath + os.sep + 'API_1-002save.edb'
# ModelPath = APIPath + os.sep + 'exAPI_1-002.edb'
# 'save file  | guardar archivo
# System.IO.Directory.CreateDirectory("c:\CSI_API_temp")
# resUnit = smodel.File.Save("C:\CSI_API_temp\example.edb")
if not os.path.isfile(ModelPath): 
    resUnit = smodel.File.Save(ModelPath)
    print("Su modelo de etabs se ha creado con exito.\nRevise en su directorio C:\\CSi_ETABS_API_Example")
else:
    print("Ya existe archivo con ese nombre, debe guradar con otro nombre.") 
smodel.SetModelIsLocked(True)


input("Enter para cerrar Etabs!")
# 'close ETABS | Cerrar aplicacion Etabs
ETABSObject.ApplicationExit(False)

# clean up variables | limpiamos las variables y eliminamos
N_mm_C = None
ETABSObject, smodel, retVersion, fullNameEtabs, resUnit = None, None, None, None, None
del N_mm_C
del ETABSObject, smodel, retVersion, fullNameEtabs, resUnit
sys.exit(-1)