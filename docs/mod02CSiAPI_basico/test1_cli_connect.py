#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Autor: F. JMucho. <fjmucho0@gmail.com>
Date: 01/04/2021
Refactorizacion.
Description:
    aquii se implementara las dependencias y la refactorizacion preliminar...
    este modulo esta en desarrollo ... no es funcional al 100% aun....
"""
import os, sys
import comtypes.client

def validate_extend(extencion=""):
    ext = None
    ext = extencion[-4:]
    if ext == ".exe":
        return True
    if ext == ".edb":
        return True
    return False
def connect_manually_to_etabs(ruta_programa="", helper=None):
    try:
        #'create an instance of the ETABS object from the specified path
        etabs_object = helper.CreateObject(ruta_programa)
        print("Conexion esitosa!.\nConexion Manual establecida")
        return etabs_object
    except (OSError, comtypes.COMError):
        # falta validar para el caso ... que se este ejecutano etabs...
        print("Cannot start a new instance of the program from " + ruta_programa)
        sys.exit(-1)
def connect_default_to_etabs(estado_manual = False):
    print("Tratando de Ejecutar etabs!.")
    #create API helper object
    helper = comtypes.client.CreateObject('ETABSv1.Helper')
    helper = helper.QueryInterface(comtypes.gen.ETABSv1.cHelper)
    
    etabs_object = None
    if estado_manual:
        ruta_programa = ""
        while True:
            print("Ejemplo de ruta: C:\\Program Files\\Computers and Structures\\ETABS 18\\ETABS.exe")
            ruta_programa = input('Ingrese la ruta del programa (etabs)> ')
            if validate_extend(ruta_programa):
                break
            print("Ingrese la ruta correcta y/o ejecutable correcto!")
        etabs_object = connect_manually_to_etabs(ruta_programa, helper)
    else:
        try:
            #create an instance of the ETABS object from the latest installed ETABS
            etabs_object = helper.CreateObjectProgID("CSI.ETABS.API.ETABSObject") 
            print("Coneccion esitosa!.")
        except (OSError, comtypes.COMError):
            print("Cannot start a new instance of the program(etabs).")
            sys.exit(-1)

    print("Ejecutando etabs!.")
    #start ETABS application | ejecutar la Aplicacion ETABS.
    etabs_object.ApplicationStart()
    # llamar la funcion que definir el tipo de plantilla/template/modelo 
    create_new_model_etabs(etabs_object)
def attach_to_instance():
    """
    """
    # Attaches to an existing ETABS application
    try:
        #get the active ETABS object | optener instancia activa de etabs.
        etabs_object = comtypes.client.GetActiveObject("CSI.ETABS.API.ETABSObject") 
        print("Coneccion exitosa!.\nadjuntando a una instancia existente.")
        create_new_model_etabs(etabs_object)
    except (OSError, comtypes.COMError):
        print("No se encontró ninguna instancia en ejecución del programa(Etabs).")

        description = """
    Para ejecutar con la Ruta manual del programa(etabs), presione la tecla 'Enter'
    en caso que quierera trabajar con la ultima version intalada ecribir 'True'

    [True] Ejecución con ruta manual del programa(etabs)
    [False] Ejecución con la ultima version instalada del programa(etbas)
    
    Presione ctrl+c (^C) para cancelar todo y salir.
    """
        print(description)
        estado_manual = input("Desea definir ruta del programa No(False)> ")
        if estado_manual: # True
            print(f"Ejecucion manual en estado: [{estado_manual}]")
            connect_default_to_etabs(True)
        elif estado_manual=="": # False
            print(f"Ejecucion por defecto!")
            connect_default_to_etabs()
        else: # ctrl+c, o otro caso
            sys.exit(-1)

def save_file_model(SapModel):
    # uso del ee05EtabsAPI_saveFile.py
    #full path to the model, set it to the desired path of your model
    APIPath = 'C:\\CSi_API_Example'
    if not os.path.exists(APIPath):
        try:
            os.makedirs(APIPath) #| intenta crear un directorio.
        except OSError:
            print("Error: "+OSError) #| si no se tiene permiso laza un error.
    ModelPath = APIPath + os.sep + 'exampleAPI_1-001.edb'
    # 'save file  | guardar archivo
    resUnit = SapModel.File.Save(ModelPath)
def open_file_model():
    # uso del ef06EtabsAPI_openFile.py
    # 'open an existing file - If no file exists, run the Save example first.
    try:
        fileName = APIPath = 'C:\\CSi_API_Example\\exAPI_1-001.edb'
    except (OSError, comtypes.COMError):
        print(f"No se puede abrir {comtypes.COMError}")
        sys.exit(-1)

def add_matials(data):
    pass
    # TODO 
def add_sections(data):
    pass
    # TODO 
def add_patterns(data):
    pass
    # TODO 
def add_cases(data):
    pass
    # TODO 
def add_combinations(data):
    pass
    # TODO 
def elements(data_files):
    pass
    # TODO 
def add_restraints(data_file):
    pass
    # TODO 
def add_joint_forces(data_file):
    pass
    # TODO

def create_new_model_etabs(etabs_connect=None):
    '''
    FORMAS DE INICIALIZAR UN MODELO
    '''
    SapModel = etabs_connect.SapModel
    # Unlocking model | Abriendo modelo (hace referencia al candadito de etabs)
    # estado_modelo = SapModel.SetModelIsLocked(False)

    # 'initialize model | Inicializa nuevo modelo en blanco
    respuesta = SapModel.InitializeNewModel()

    msg="Defina el tipo de modelo, con la cual trabajar"
    print(f"{msg}\n"+"="*len(msg))
    print("[1] new black model\n[2] grid-only template model\n[3] steel deck template model\n[4] Open file model")
    tipo_modelo = input('> ') # aquii se puede validar para ingresos solo a numeros
    if tipo_modelo=="1":
        print("create new blank model | crea una nueva hoja en blanco")
        respuesta = SapModel.File.NewBlank()
        # close_etabs(etabs_connect)# prueba, aquii ya dentra otro menu para guardar o hacer diseño ...
        # TODO
        # save_file_model()
    if tipo_modelo=="2":
        print("create grid-only template model | Crea una nueva hoja con grilla")
        respuesta = SapModel.File.NewGridOnly(4,12,12,4,4,24,24)
        # close_etabs(etabs_connect)# prueba, aquii ya dentra otro menu para guardar o hacer diseño ...
        # TODO
        # save_file_model()
    if tipo_modelo=="3":
        print("create steel deck template model | Crea una nueva hoja de tipo ...")
        respuesta = SapModel.File.NewSteelDeck(4,12.0,12.0,4,4,24.0,24.0)
        # close_etabs(etabs_connect)# prueba, aquii ya dentra otro menu para guardar o hacer diseño ...
        # TODO
        # save_file_model()
    if tipo_modelo=="4":
        print("Open | Abrir\nAun no esta implementado!...")
        create_new_model_etabs(etabs_connect)
        # TODO
    if tipo_modelo=="":
        print("No contamos con otro tipo de plantilla definida.\nDefina con la que contamos")
        create_new_model_etabs(etabs_connect)
    else:
        print("No tenemos este modulo!...")
        close_etabs(etabs_connect)
    # return

def version_of_etabs(SapModel=None):
    fullNameEtabs = []
    # Retrieve information about the program | ... informacion del programa
    fullNameEtabs = SapModel.GetProgramInfo()
    return fullNameEtabs
def close_etabs(etabs_connect=None):
    print("Antes de cerrar, sedea guardar modelo?, en caso que no ponga cancelar ...")
    etabs_connect.ApplicationExit(True) 
    print("Close the program | Cerrar la aplicacion")
    sys.exit(-1)

if __name__ == '__main__':
    # version_of_etabs()
    attach_to_instance() 
    # TODO, falta implementar menu