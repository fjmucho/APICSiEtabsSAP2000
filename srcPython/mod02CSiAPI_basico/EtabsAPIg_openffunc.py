#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
**************** 0 ******************
@date: 06/04/21 to 20/04/21
@author: F. JMucho. <fjmucho0@gmail.com>
@Description: implelemntacion en una funcion
**************** 0 ******************
"""
def validate_extend(extencion=""):
    ext = None
    ext = extencion[-4:].lower()
    if ext == ".edb":
        return True
    return False
def openFile(smodel=None, name_file=""):
    # if os.path.isfile(name_file):
    #     SetIcon(wx.Icon(name_file)
    # archivo='untitled.edb'
    # f_ext = name_file[-4:]
    ok = validate_extend(name_file)
    if ok:
        try:
            fileName = name_file
            # print(fileName)
        except (OSError, comtypes.COMError):
            print(f"No se puede abrir {comtypes.COMError}")
            return False, None
        
        # smodel.SetModelIsLocked(False)
        # crea el lienzo vacio equivalente a figure en matplotlib
        smodel.InitializeNewModel()
        
        resUnit = smodel.File.OpenFile(fileName)
        
        infoProject = []
        infoProject = smodel.GetProjectInfo()
        print(infoProject) # la informacion dependera de usario registrado
        print("Abriendo!.")
    else:
        print("La extension no es valida, o no es un archivo etabs!.")
        return True, None
    return True, resUnit


if __name__ == '__main__':
    import  sys
    # from EtabsAPIa_connfunc import connect_to_etabs
    # on_status, smodel, eobj = False, None, None
    # # evaluamos si ya tenemos la coneccion a etabs
    # if eobj == None:
    #     on_status, eobj = connect_to_etabs()
    #     if on_status==False: sys.exit(-1)

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

    nombre_archivo = "API_1-002open.EDB"
    archivo = 'C:\\CSi_ETABS_API_Example\\' + nombre_archivo
    ok, newSapModel = openFile(smodel,  archivo)


    input("Enter para cerrar Etabs!")
    # Close the program | Cerrar la aplicacion
    eobj.ApplicationExit(False)

    smodel, eobj = None, None
    newSapModel, nombre_archivo,    archivo = None, None, None
    del smodel, eobj, newSapModel, nombre_archivo,  archivo
    sys.exit(-1)