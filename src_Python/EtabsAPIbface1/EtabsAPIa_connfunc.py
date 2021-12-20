#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
**************** 0 ******************
@date: 06/04/21 to 20/04/21
@author: F. JMucho. <fjmucho0@gmail.com>
@Description: implelemntacion en una funcion
**************** 0 ****************** 
"""
import sys
import comtypes.client

def connect_to_etabs():
    on_status = False
    ETABSObject = None
    try:
        ETABSObject = comtypes.client.GetActiveObject("CSI.ETABS.API.ETABSObject")
        print("Coneccion establecida!.\nadjuntando a una instancia existente.")
        on_status = True
    except (OSError, comtypes.COMError):
        print("No se encontro ninguna instancia en ejecucion del programa(Etabs).")
    return on_status, ETABSObject, # _=smodel


if __name__ == '__main__':
    eobj = None
    on_status=False
    
    on_status, eobj = connect_to_etabs()
    if on_status==False: exit()

    print("La sesión actual de este programa se conectó haciendo uso de la API. \
Se recomenda que cierre este programa utilizando el programa desde el que se inició.")
    input("Enter para cerrar Etabs!")
    # Close the program | Cerrar la aplicacion
    eobj.ApplicationExit(False)

    eobj, smodel, on_status  = None, None, None
    del smodel, eobj, on_status
    sys.exit(-1)