#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Para usar esta script tiene que estar ejecutandose Etabs.

Estructura algoritmo.
    establecer conexion
    Cerramos la aplicacion.

Methods.: conexion
    comtypes.client
        .GetActiveObject(Progit, interface=None, dynamic=False)
            .ApplicationExit(FileSave)

Progit      : es un cadena, str
interface   : in objeto no definido, None.
dynamic     : es un booleano, bool
"""
import sys
# import | importar la libreria requerida
import comtypes.client


try:
    # Connecting | coneccion
    ETABSObject = comtypes.client.GetActiveObject("CSI.ETABS.API.ETABSObject")
    print("Conexion exitosa!.")
except (OSError, comtypes.COMError):
    # No running instance of the program found or failed to attach.
    print("No se encontró ninguna instancia en ejecución del programa(Etabs).")
    sys.exit(-1)

# Close the program | Cerrar la aplicacion
ETABSObject.ApplicationExit(True) 

# clean up variables | limpiamos la variable y eliminamos
ETABSObject = None
del ETABSObject

# Show list of methods and properties | Muestra la lista de metodos y propiedades
# print(dir(ETABSObject)) # 
sys.exit(-1)

'''
['AddRef', 'ApplicationExit', 'ApplicationStart', 'ApplicationStart_2', 'GetIDsOfNames', 
'GetOAPIVersionNumber', 'GetTypeInfo', 'GetTypeInfoCount', 'Hide', 'Invoke', 'QueryInterface', 'Release', 
'SapModel', 
'SetAsActiveObject', 'Unhide', 'UnsetAsActiveObject', 'Visible', '_AddRef',
'_GetIDsOfNames', '_GetTypeInfo', '_IDispatch__com_GetIDsOfNames', '_IDispatch__com_GetTypeInfo', 
'_IDispatch__com_GetTypeInfoCount', '_IDispatch__com_Invoke', '_IUnknown__com_AddRef', 
'_IUnknown__com_QueryInterface', '_IUnknown__com_Release', '_Invoke', '_QueryInterface', '_Release', 
...
'_b_base_', '_b_needsfree_', '_cOAPI__com_ApplicationExit', '_cOAPI__com_ApplicationStart', 
'_cOAPI__com_ApplicationStart_2', '_cOAPI__com_GetOAPIVersionNumber', '_cOAPI__com_Hide', 
'_cOAPI__com_SetAsActiveObject', '_cOAPI__com_Unhide', '_cOAPI__com_UnsetAsActiveObject', 
'_cOAPI__com_Visible', '_cOAPI__com__get_SapModel', '_case_insensitive_', '_compointer_base__get_value', 
'_idlflags_', '_iid_', '_invoke', '_methods_', '_needs_com_addref_', '_objects', '_type_', 'from_param', 
'value']
'''