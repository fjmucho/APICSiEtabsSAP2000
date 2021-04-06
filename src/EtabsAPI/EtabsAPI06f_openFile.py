#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Autor: F. JMucho. <fjmucho0@gmail.com>
Date: 
Description:
* Etbas debe de estar ejecutandose.

    Algoritmo:
        
        evaluar si, esta en ejecucion una instalcia de etabs
            adjuntar la instancia a la existente
            mensaje: coneccion exitosa
        caso contrario:
            lanzar un mesaje y terminar
        ya puedes hacer operaciones con etbas
        crear un objeto etbas
        mantener cerrado ...
        inicializar un nuevo modelo de tipo 
        
    cFile Methods/Metodos.: abrir archivo (modelo)
        ...
        .SapModel.GetProjectInfo()
            ...
            .OpenFile()     	'Opens an existing file.
            ...
        ...
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

# 'initialize model | Inicializa nuevo modelo en blanco
resUnit = SapModel.InitializeNewModel()


# 'open an existing file - If no file exists, run the Save example first.
try:
	fileName = APIPath = 'C:\\CSi_ETABS_API_Example\\exAPI_1-001.edb'
except (OSError, comtypes.COMError):
    print(f"No se puede abrir {comtypes.COMError}")
    sys.exit(-1)
resUnit = SapModel.File.OpenFile(fileName)


infoProject = []
# Retrieves the project information data. | 
infoProject = SapModel.GetProjectInfo()
print(infoProject) # la informacion dependera de usario registrado
# [4, 
# ('Company Name', 'Revision Number', 'GUID', 'Model Version'), 
# ('unap', '0', '2e2d75e3-12bc-4837-8a3e-02425542cbb7', '1'), 
# 0]
# se puede explicar: 4 parametros, 
# cabeceras[nombreCompania, numeroRevision, GUID, versionModelo]=[..., ..., ..., ...]

# Unit Preferences | Preferencias de Unidad
N_mm_C = 6 # kN_mm_C
SapModel.SetPresentUnits(N_mm_C)

# get database units | Optener las unidades de la base de datos
dbUnits = None
dbUnits = SapModel.GetDatabaseUnits()
print(dbUnits) # vemos que solo contamos con una unidad asignada 'N_mm_C'

# clean up variables | limpiamos las variables y eliminamos
del N_mm_C
ETABSObject, SapModel, retVersion, fullNameEtabs, resUnit, fileName, infoProject = None, None, None, None, None, None, None
del ETABSObject, SapModel, retVersion, fullNameEtabs, resUnit, fileName, infoProject
sys.exit()