#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
""" 
Para usar esta script tiene que estar ejecutandose Etabs.

Nuevo: file 'untitled'
Methods.: nuevo modelo
    comtypes.client
        .GetActiveObject(Progit, interface=None, dynamic=False)
        .SapModel
            .InitializeNewModel()
            .GetProgramInfo()
        .SapModel.File
            .NewBlank()     | used
            .NewGridOnly()  | used
            .NewSteelDeck() | used
            ...
            .New2DFrame()   | not used now
            .New3DFrame()   | not used now
            .NewBeam()      | not used now
            .NewSolidBlock()| not used now
"""
import os, sys
import comtypes.client

try:
    # Connecting | coneccion
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
# get value | Optner el valor.
print(SapModel.GetModelIsLocked()) # False


# 'initialize model | Inicializa nuevo modelo en blanco
resUnit = SapModel.InitializeNewModel()

# print(dir(SapModel.File)) # optenemos los metodos y propiedades para usar
# print(help(SapModel.File.New2DFrame)) # intentando optener informacion...
for nombre in dir(SapModel.File.New2DFrame):
    if nombre.startswith('__') or nombre.startswith('_'):
        continue
    print(f"{nombre}")


#create new blank model | crea una nueva hoja en blanco
resUnit = SapModel.File.NewBlank()

mergeTol = [0.45, 0.70]
resUnit = SapModel.SetMergeTol(mergeTol)
print(SapModel.GetMergeTol()) # [0.45, 0]

# Unit Preferences | Preferencias de Unidad
N_mm_C = 6
SapModel.SetPresentUnits(N_mm_C)
# get present units | Optener la presente unidad(s)
print(SapModel.GetPresentUnits()) # 6


# clean up variables | limpiamos las variables y eliminamos
mergeTol, N_mm_C = None, None
del mergeTol, N_mm_C
ETABSObject, SapModel, retVersion, fullNameEtabs = None, None, None, None
del ETABSObject, SapModel, retVersion, fullNameEtabs
sys.exit()

'''
['AddRef', 'GetFilePath', 'GetIDsOfNames', 'GetTypeInfo', 'GetTypeInfoCount', 'Invoke', 
'New2DFrame', 
'New3DFrame', 
'NewBeam', 
'NewBlank', 
'NewGridOnly', 
'NewSolidBlock', 
'NewSteelDeck', 
'NewWall', 
'OpenFile', 'QueryInterface', 'Release', 
'Save', 
'_AddRef', '_GetIDsOfNames', '_GetTypeInfo', '_IDispatch__com_GetIDsOfNames', 
'_IDispatch__com_GetTypeInfo', '_IDispatch__com_GetTypeInfoCount', '_IDispatch__com_Invoke', 
'_IUnknown__com_AddRef', '_IUnknown__com_QueryInterface', '_IUnknown__com_Release', '_Invoke', 
'_QueryInterface', '_Release', 
...
'_b_base_', '_b_needsfree_', '_cFile__com_GetFilePath', 
'_cFile__com_New2DFrame', '_cFile__com_New3DFrame', '_cFile__com_NewBeam', '_cFile__com_NewBlank', 
'_cFile__com_NewGridOnly', '_cFile__com_NewSolidBlock', '_cFile__com_NewSteelDeck', 
'_cFile__com_NewWall', '_cFile__com_OpenFile', '_cFile__com_Save', '_case_insensitive_', 
'_compointer_base__get_value', '_idlflags_', '_iid_', '_invoke', '_methods_', '_needs_com_addref_', 
'_objects', '_type_', 'from_param', 'value']
'''