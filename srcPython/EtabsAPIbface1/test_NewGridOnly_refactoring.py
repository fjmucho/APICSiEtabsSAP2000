#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Description: algoritmo de instrucciones:

        evaluar si: esta en ejecucion una instancia de etabs
            adjuntar la instancia a la existente
        caso contrario:
            evaluar si esta definido coneccion manual:
                ejecutar via ruta manual
            caso contrario:
                busco la ultima verion instalada de etabs intentar conectarme 
                si coneccion es esitosa:
                lanzar mensage: coneccion exitosa
            ejecutar etabs

Methods.:
    comtypes.client
        .GetActiveObject()
        .ApplicationStart()
        .CreateObject()
            .QueryInterface()
            .CreateObjectProgID()
        .ApplicationStart()
"""
import os, sys
import comtypes.client

# Variable para definir una instancia manual para Etabs.
rutaEspecifica = False

#if the above flag is set to True, specify the path to ETABS below
# si la bandera anterior se establece en True, entonces debe especificar la ruta a ETABS a continuación
ProgramPath = "C:\\Program Files\\Computers and Structures\\ETABS 19\\ETABS.exe"


try:
    #get the active ETABS object
    ETABSObject = comtypes.client.GetActiveObject("CSI.ETABS.API.ETABSObject")
    print("Coneccion exitosa!.\nadjuntando a una instancia existente.")
except (OSError, comtypes.COMError):
    # No running instance of the program found or failed to attach.
    print("No se encontró ninguna instancia en ejecución del programa(Etabs).")

    print("Tratando de Ejecutar etabs!.")
    #create API helper object
    helper = comtypes.client.CreateObject('ETABSv1.Helper')
    helper = helper.QueryInterface(comtypes.gen.ETABSv1.cHelper)
    if rutaEspecifica:
        try:
            #'create an instance of the ETABS object from the specified path
            ETABSObject = helper.CreateObject(ProgramPath)
            print("Coneccion esitosa!.\nConexion Manual")
        except (OSError, comtypes.COMError):
            print("Cannot start a new instance of the program from " + ProgramPath)
            sys.exit(-1)
    else:
        try: 
            #create an instance of the ETABS object from the latest installed ETABS
            ETABSObject = helper.CreateObjectProgID("CSI.ETABS.API.ETABSObject") 
            print("Coneccion esitosa!.")
        except (OSError, comtypes.COMError):
            print("Cannot start a new instance of the program.")
            sys.exit(-1)
    print("Ejecutando etabs!.")
    #start ETABS application | ejecutar la Aplicacion ETABS.
    ETABSObject.ApplicationStart()

#create SapModel object | crea instancia del objeto SapModel
smodel = ETABSObject.SapModel
# Unlocking model | Abriendo modelo para establecer dibujo y ejecucion (hace referencia al candadito de etabs)
smodel.SetModelIsLocked(False)
# 'initialize model | Inicializa una hoja en blanco para definir un modelo
res = smodel.InitializeNewModel()
# create grid-only template model | Crea una nueva hoja con grilla
res = smodel.File.NewGridOnly(4,12,12,4,4,24,24)

# Unit Preferences | Preferencias de Unidad
N_mm_C = 6 #kN_m_c
smodel.SetPresentUnits(N_mm_C)

# Materials | materiales
smodel.PropMaterial.SetMaterial("CONC35", 2)

smodel.PropMaterial.SetOConcrete_1("CONC35", 35, False, 0, 1, 2, 0.0022, 0.0052, -0.1, 0, 0)

# Sections | secciones
sectionName = 'ConcSection'
smodel.PropFrame.SetRectangle(sectionName, "CONC35", 400, 400)

# Patterns | patrones
ret = smodel.LoadPatterns.Add("LCASE1", 2)
ret = smodel.LoadPatterns.Add("LCASE2", 3)
# print(ret)

# Cases | casos
ret = smodel.LoadCases.StaticLinear.SetCase("LCASE1")
ret = smodel.LoadCases.StaticLinear.SetCase("LCASE1")

# Combinations | combinaciones
ret = smodel.RespCombo.Add("COMB1", 0)

CNameType = 0
ret = smodel.RespCombo.SetCaseList("COMB1", CNameType, "LCASE1", 1.25)
ret = smodel.RespCombo.SetCaseList("COMB1", CNameType, "LCASE2", 1.5)

NumberItems = 0
CNameType = []
CName = []
SF = []
smodel.RespCombo.GetCaseList("COMB1", NumberItems, CNameType, CName, SF)

# Elements | elementos
FrameName1 = ' '
FrameName2 = ' '
FrameName3 = ' '
[FrameName1, ret] = smodel.FrameObj.AddByCoord(0, 0, 0, 0, 0, 10, FrameName1, sectionName, '1', 'Global')
[FrameName2, ret] = smodel.FrameObj.AddByCoord(0, 0, 10, 8, 0, 16, FrameName2, sectionName, '2', 'Global')
[FrameName3, ret] = smodel.FrameObj.AddByCoord(-4, 0, 10, 0, 0, 10, FrameName3, sectionName, '3', 'Global')

# Assigning restraints
PointName1 = ' '
PointName2 = ' '
Restraint = [True, True, True, True, True, True]
[PointName1, PointName2, ret] = smodel.FrameObj.GetPoints(FrameName1, PointName1, PointName2)
ret = smodel.PointObj.SetRestraint(PointName1, Restraint)

# Joint forces | juntas o fuerzas conjuntas

Value = (100.0, 0.0, 0.0, 0.0, 0.0, 0.0)
Value2 = [0.0, 200.0, 0.0, 0.0, 0.0, 0.0]

ret = smodel.PointObj.SetLoadForce("4", "LCASE1", Value, True, 'Global', 0)
ret = smodel.PointObj.SetLoadForce('3', 'LCASE2', Value2, True, 'Global', 0)


#save model | guardar nuestro modelo
#full path to the model, set it to the desired path of your model
APIPath = 'C:\\CSi_ETABS_API_Example'
if not os.path.exists(APIPath):
    try:
        os.makedirs(APIPath) #| intenta crear un directorio.
    except OSError:
        print("Error: "+OSError) #| si no se tiene permiso laza un error.
ModelPath = APIPath + os.sep + 'tutorial3.edb'
ret = smodel.File.Save(ModelPath)
# 'display the filename of the model
print(smodel.GetModelFilename())

#run model (this will create the analysis model)
ret = smodel.Analyze.RunAnalysis()

# deselect all cases and combos
ret = smodel.Results.Setup.DeselectAllCasesAndCombosForOutput

# set combo selected for output
ret = smodel.Results.Setup.SetComboSelectedForOutput("COMB1")

# Get frame forces | optener nuestro marco de fuerzas
ObjectElm = 0
NumberResults = 0
Obj = []
ObjSta = []
Elm = []
ElmSta = []
LoadCase = []
StepType = []
StepNum = []
P = []
V2 = []
V3 = []
T = []
M2 = []
M3 = []

try:
    ret = smodel.Results.FrameForce(FrameName1, ObjectElm, NumberResults, Obj, ObjSta, Elm, ElmSta, LoadCase, StepType, StepNum, P, V2, V3, T, M2, M3)
    # ret = smodel.Story.GetStories()
except (OSError, comtypes.COMError):
    print("Error ...", OSError, comtypes.COMError)
print(ret)

# Close the program | Cerrar la aplicacion
ETABSObject.ApplicationExit(False)

# clean up variables | limpiamos las variables y eliminamos
ETABSObject, SapModel, res = None, None, None
del ETABSObject, SapModel, res