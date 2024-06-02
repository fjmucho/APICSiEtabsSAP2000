#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" 
**************** 0 ******************
@date: 06/04/21 to 20/04/21
@author: F. JMucho. <fjmucho0@gmail.com>
@Description: implelemntacion en una funcion
**************** 0 ****************** 
"""
def newMNewBlank(smodel=None):
    #create new blank model | crea una nueva hoja en blanco
    return smodel.File.NewBlank()

def newMNewGridOnly(smodel=None, grid_values=[]):
    # create grid-only template model
    return smodel.File.NewGridOnly(
        grid_values[0],grid_values[1],
        grid_values[2],grid_values[3],
        grid_values[4],grid_values[5], grid_values[6])

def newMNewSteelDeck(smodel=None, sgrid_values=[]):
    # create steel deck template model
    return smodel.File.NewSteelDeck(
        sgrid_values[0],sgrid_values[1],
        sgrid_values[2],sgrid_values[3],
        sgrid_values[4],sgrid_values[5], sgrid_values[6])

if __name__ == '__main__':
    import sys
    on_status, eobj = False, None
    # ============== codigo que ejecuta por defecto a etbas =============
    from EtabsAPIb_zconn_funcion import *
    on_status, eobj = attach_to_instance() # instancia por ejecucion
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

    # ============ 
    # create SapModel object | Crea la instancia al objeto SapModel (Area de trabajo)
    smodel = eobj.SapModel
    smodel.SetModelIsLocked(False)
    # crea el lienzo vacio equivalente a figure en matplotlib
    # 'initialize model | Inicializa nuevo modelo en blanco
    smodel.InitializeNewModel()


    new_model_ax = None
    # new_model_ax = newMNewBlank(smodel)
    grid_values = [4,12,12,4,4,24,24]
    new_model_ax = newMNewGridOnly(smodel, grid_values)
    # sgrid_values = [4,12,12,4,4,24,24]
    # new_model_ax = newMNewSteelDeck(smodel, sgrid_values)

    smodel.SetModelIsLocked(True)

    input("Enter para cerrar Etabs!")
    # Close the program | Cerrar la aplicacion
    eobj.ApplicationExit(False)

    smodel, eobj = None, None
    new_model_ax, grid_values, sgrid_values = None, None, None
    del smodel, eobj, new_model_ax
    sys.exit(-1)