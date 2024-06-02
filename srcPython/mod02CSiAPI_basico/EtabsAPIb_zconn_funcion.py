#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
**************** 0 ******************
@date: 06/04/21 to 20/04/21
@author: F. JMucho. <fjmucho0@gmail.com>
@Description: implelemntacion en una funcion
**************** 0 ******************
"""
import os, sys
import comtypes.client

def not_connect(): 
    print("No se pudo conectar...")
    sys.exit(-1)
def connect_manually_to_etabs(ruta_programa=""):
    print("Tratando de Ejecutar etabs!.")
    helper = comtypes.client.CreateObject('ETABSv1.Helper')
    helper = helper.QueryInterface(comtypes.gen.ETABSv1.cHelper)
    on_status = False
    ETABSObject = None
    try:
        ETABSObject = helper.CreateObject(ruta_programa)
        print("Conexion esitosa!.\nConexion Manual establecida")
    except (OSError, comtypes.COMError):
        print("Cannot start a new instance of the program from " + ruta_programa)
        return False, ETABSObject
    print("Ejecutando etabs!.")
    ETABSObject.ApplicationStart()
    return True, ETABSObject
def connect_default_to_etabs():
    print("Tratando de Ejecutar etabs!.")
    helper = comtypes.client.CreateObject('ETABSv1.Helper')
    helper = helper.QueryInterface(comtypes.gen.ETABSv1.cHelper)
    ETABSObject = None
    try:
        ETABSObject = helper.CreateObjectProgID("CSI.ETABS.API.ETABSObject") 
        print("Coneccion esitosa!.")
    except (OSError, comtypes.COMError):
        print("Cannot start a new instance of the program(etabs).")
        return False, ETABSObject
    print("Ejecutando etabs!.")
    ETABSObject.ApplicationStart()
    return True, ETABSObject
def attach_to_instance():
    """ coneccion a etabs """
    on_status = False
    ETABSObject = None
    try:
        ETABSObject = comtypes.client.GetActiveObject("CSI.ETABS.API.ETABSObject") 
        print("Coneccion exitosa!.\nadjuntando a una instancia existente.")
        on_status = True
    except (OSError, comtypes.COMError):
        print("No se encontró ninguna instancia en ejecución del programa(etabs).")
    return on_status, ETABSObject, # _=smodel

if __name__ == '__main__':
    '''ALGORITMO:
    adjuntar es posible?:
        adjuntar.
    con ruta manual adjuntar es posible?:
        adjuntar.
    buscar ultima instalacion de etabs y adjuntar es posible?:
        adjuntar.
    si no se pudo:
        terminar.
    '''
    on_status, eobj = False, None
    on_status, eobj = attach_to_instance() # instalcia por ejecucion

    estado_manual = False
    if on_status==False:
        ruta_programa =""
        if estado_manual: # instancia por conecion manual
            ruta_programa = "C:\\Program Files\\Computers and Structures\\ETABS 17\\ETABS.exe"
            on_status, eobj = connect_manually_to_etabs(ruta_programa)
            if not on_status: not_connect()
        else: # instancia por conecion por defecto
            on_status, eobj = connect_default_to_etabs()
    if not on_status: not_connect()

    smodel = None
    smodel = eobj.SapModel

    input("Enter para cerrar Etabs!")
    # Close the program | Cerrar la aplicacio
    eobj.ApplicationExit(False)
    
    estado_manual, on_status, eobj, smodel = None, None, None, None
    del on_status, eobj, smodel, estado_manual
    sys.exit(-1)