#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
**************** 0 ******************
@date: 06/04/21 to 20/04/21
@author: F. JMucho. <fjmucho0@gmail.com>
@Description:
**************** 0 ******************
"""
import os, sys

def saveAsFile(smodel=None, APIPath='C:\\CSi_API_Example', name_file='example.edb'):

    if not os.path.exists(APIPath):
        try: os.makedirs(APIPath)
        except OSError:
            print("Error: "+OSError+", o no tienes permisos...")
            return False, None
    resUnit = None
    file_ext = []
    if not os.path.isfile(APIPath + os.sep + name_file): 
        file_ext = name_file[-4:] # extrae la parte .edb
        ModelPath = ""
        if file_ext == ".edb": ModelPath = APIPath + os.sep + name_file
        else: ModelPath = APIPath + os.sep + name_file+".edb"
        resUnit = smodel.File.Save(ModelPath)
        print(f"Su modelo de etabs se ha creado con exito.\nRevise en su directorio {APIPath}")
        return True, resUnit
    else:
        print("Ya existe archivo con ese nombre, debe guradar con otro nombre.")
        # input("Ingrese nombre: ")
        return False, resUnit


if __name__ == '__main__':
    # # conecion
    # from EtabsAPIa_connfunc import connect_to_etabs
    # on_status, smodel, eobj = False, None, None
    # # evaluamos si ya tenemos la coneccion a etabs
    # if eobj == None:
    #     on_status, eobj = connect_to_etabs()
    #     if on_status==False: sys.exit(-1)

    # smodel = eobj.SapModel
    # smodel.SetModelIsLocked(False)
    # # crea el lienzo vacio equivalente a figure en matplotlib
    # smodel.InitializeNewModel()
    # # creacion del modelo
    # newSapModel = None
    # from EtabsAPId_NMfunc import newMNewSteelDeck
    # sgrid_values = [4,12,12,4,4,24,24]
    # newSapModel = newMNewSteelDeck(smodel, sgrid_values)

    on_status, eobj = False, None
    # ============== codigo que ejecuta por defecto a etbas =============
    from EtabsAPIb_zconn_funcion import *
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

    # create SapModel object | Crea la instancia al objeto SapModel (Area de trabajo)
    smodel = eobj.SapModel
    smodel.SetModelIsLocked(False)
    # crea el lienzo vacio equivalente a figure en matplotlib
    # 'initialize model | Inicializa nuevo modelo en blanco
    smodel.InitializeNewModel()

    # ============= codigo para crear un nuevo modelo =========
    from EtabsAPId_nmfunc import *
    new_model_ax = None
    # new_model_ax = newMNewBlank(smodel)
    grid_values = [4,12,12,4,4,24,24]
    new_model_ax = newMNewGridOnly(smodel, grid_values)

    # ===== codigo para Guardar el archivo o modelo creado =====
    ruta_directorio = "C:\\CSi_API_Example"
    nombre_Archivo = "API_1-002save.edb"
    on_status, newSapModel = saveAsFile(smodel, ruta_directorio, nombre_Archivo)
    if on_status==False: print("No se pudo guardar...")


    input("Enter para cerrar Etabs!")
    # Close the program | Cerrar la aplicacion
    eobj.ApplicationExit(False)

    smodel, eobj = None, None
    newSapModel, ruta_directorio, nombre_Archivo = None, None, None
    del smodel, eobj, newSapModel, ruta_directorio, nombre_Archivo
    sys.exit(-1)