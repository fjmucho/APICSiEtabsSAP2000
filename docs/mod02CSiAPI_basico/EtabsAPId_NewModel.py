#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
""" 
cFile: Para usar esta script tiene que estar ejecutandose Etabs.
Nuevo archivo: 'untitled'

Metodos - cFile
    comtypes.client
        .GetActiveObject(Progit, interface=None, dynamic=False)
        .SapModel
            .InitializeNewModel()
            .GetProgramInfo()
        .SapModel.File
            .NewBlank()        'Creates a new, blank model.
            .NewGridOnly()     'Creates a new grid-only model from template.
            .NewSteelDeck()    'Creates a new steel deck model from template.
            .OpenFile()        'Opens an existing file.
            .Save()            'Saves the present model.

params: NewGridOnly, NewSteelDeck
    NewGridOnly(
        double numero_de_pisos, double BottomStoryHeight, 
        int NumberLinesX, int NumberLinesY, 
        double SpacingX, double SpacingY)
examples: NewSteelDeck(4,12.0,12.0,4,4,24.0,24.0)
"""
import os, sys
import comtypes.client

try:
    EtabsObject = comtypes.client.GetActiveObject("CSI.ETABS.API.ETABSObject")
    print("Coneccion exitosa!.\nadjuntando a una instancia existente.")
except (OSError, comtypes.COMError):
    print("No se encontró ninguna instancia en ejecución del programa(Etabs).")
    sys.exit(-1)
# create SapModel object | Crea el objeto Modelo
smodel = EtabsObject.SapModel

# Unlocking model | Mantener Cerrado modelo (hace referencia al candadito de etabs)
smodel.SetModelIsLocked(False)
# get value | Optner el valor.
print(smodel.GetModelIsLocked()) # False

# 'initialize model | Inicializa un nuevo lienzo en blanco
# resUnit = smodel.InitializeNewModel # este tambien es aceptado, pero es un metodo sin parametros
smodel.InitializeNewModel()

# print(dir(smodel.File)) # optenemos los metodos y propiedades para usar
# print(help(smodel.File.New2DFrame)) # intentando optener informacion...
for nombre in dir(smodel.File.New2DFrame):
    if nombre.startswith('__') or nombre.startswith('_'):
        continue
    print(f"{nombre}")

# === FORMAS DE INICIALIZAR UN MODELO ===
#create new blank model | crea una nueva hoja en blanco
resUnit = smodel.File.NewBlank()
# # create grid-only template model - [pisos, ]
# resUnit = smodel.File.NewGridOnly(4, 12,12, 4,4, 24,24)
# # create steel deck template model
# resUnit = smodel.File.NewSteelDeck(4, 12.0,12.0, 4,4, 24.0,24.0)


# Unit Preferences | Preferencias de Unidad
N_mm_C = 6
smodel.SetPresentUnits(N_mm_C)
# get present units | Optener la presente unidad(s)
print(smodel.GetPresentUnits()) # 6

# sintasis: SetMergeTol(double MergeTol)
mergeTol = 0.45
resUnit = smodel.SetMergeTol(mergeTol)
print(smodel.GetMergeTol()) # [0.45, 0]

smodel.SetModelIsLocked(True)

input("Enter para cerrar Etabs!")
# Close the program | Cerrar la aplicacion
EtabsObject.ApplicationExit(False)

# clean up variables | limpiamos las variables y eliminamos
mergeTol, N_mm_C = None, None
del mergeTol, N_mm_C
EtabsObject, smodel, retVersion, fullNameEtabs = None, None, None, None
del EtabsObject, smodel, retVersion, fullNameEtabs
sys.exit()

'''
['AddRef', 'GetFilePath', 'GetIDsOfNames', 'GetTypeInfo', 'GetTypeInfoCount', 
'Invoke', 'New2DFrame', 'New3DFrame', 'NewBeam', 'NewBlank', 'NewGridOnly', 
'NewSolidBlock', 'NewSteelDeck', 'NewWall', 'OpenFile', 'QueryInterface', 
'Release', 'Save',  
...
'_objects', '_type_', 'from_param', 'value']
'''