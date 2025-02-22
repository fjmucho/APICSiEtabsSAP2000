#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
| ----------------------------------------------------------------------- 
| Cercha o armadura. - ejecucion en API de CSi
| -----------------------------------------------------------------------
| description: EL script esta preparado para que se ejecute tanto en SAP200 y ETABS
|              y es posible ejecutar con algunas modificaciones en otras como BRIDGE 
|              y SAFE, ............................................................. 
|              Si gustas puedes crear una copia en github en una rama secundaria y 
|              actualizar a tu gusto con las otras aplicaciones de CSiAPI.
| ref: C:\\Program Files\\Computers and Structures\\ETABS 17\\CSI API ETABS v1.chm
|      youtube: ....
| author: fjmucho0@gmail.com
| date created: 04/02/2021 
| date updated: 06/07/2024
"""

import os, sys
import numpy as np
import comtypes.client

# | definicion de Geometria de la estructura ----------------------------

# add point object
nodes = np.array([
    [-37.5, 0, 200],
    [37.5, 0, 200],
    [-37.5, 37.5, 100],
    [37.5, 37.5, 100],
    [37.5, -37.5, 100],
    [-37.5, -37.5, 100],
    [-100, 100, 0],
    [100, 100, 0],
    [100, -100, 0],
    [-100, -100, 0]
    ])

# add frame object by coordinates
elems = np.array([
    [0,1],
    [3,2],
    [2,1],
    [4,0],
    [5,1],
    [3,1],
    [4,1],
    [2,0],
    [5,0],
    [5,2],
    [4,3],
    [2,3],
    [5,4],
    [9,2],
    [6,5],
    [8,3],
    [7,4],
    [6,3],
    [7,2],
    [9,4],
    [8,5],
    [9,5],
    [6,2],
    [7,3],
    [8,4]
    ])

nn = np.shape(nodes)[0]
ne = np.shape(elems)[0]


# Indicar el programa a usar
connect_to = 1; #1 para SAP2000 y 2 para ETABS
# Variable para definir una instancia manual para el programa y definir la ruta.
porRuta = False # 0=False o 1=True

# | Comandos y funciones de API CSI ---------------------------------------

smodel, response_status = None, None
conn = {};

if connect_to == 1:  # SAP2000
    name_app="SAP2000"
    conn = {
        'app_ruta': "C:\\Program Files\\Computers and Structures\\SAP2000 26\\SAP2000.exe",
        'app_adjunto': f"CSI.SAP2000.API.SapObject",
        'app_helper': 'SAP2000v1.Helper'
    }
elif (connect_to == 2): # ETABS
    name_app="ETABS"
    conn = {
        'app_ruta': "C:\\Program Files\\Computers and Structures\\ETABS 21\\ETABS.exe",
        'app_adjunto': "CSI.ETABS.API.ETABSObject",
        'app_helper': "ETABSv1.Helper"
    }
# elif (connect_to == 3): # SAFE
#     name_app="SAFE"
#     conn = {
#     }
else: 
    print("No tenemos soporte aun")
    sys.exit()

try:
    connect_to_app = comtypes.client.GetActiveObject(conn['app_adjunto'])
    print("Coneccion exitosa!.\nadjuntando a una instancia existente.")
except (OSError, comtypes.COMError):
    print(f"No se encontró ninguna instancia en ejecución del {name_app}.")

    print(f"Tratando de Ejecutar {name_app}!.")
    #create API helper object
    helper = comtypes.client.CreateObject(conn['app_helper'])
    if connect_to == 1:
        helper = helper.QueryInterface(comtypes.gen.SAP2000v1.cHelper)
    else:
        helper = helper.QueryInterface(comtypes.gen.ETABSv1.cHelper);
    # helper = comtypes.client.CreateObject(conn['app_helper']).QueryInterface()
    if porRuta: # para versiones anteriores a la ultima version instalada
        ProgramPath = conn['app_ruta'];
        try:
            connect_to_app = helper.CreateObject(ProgramPath)
            print("Coneccion establecida!.\nConexion Manual")
        except (OSError, comtypes.COMError):
            print("Cannot start a new instance of the program from " + ProgramPath)
            sys.exit(-1)
    else:
        try: 
            connect_to_app = helper.CreateObjectProgID(conn['app_adjunto']) 
            print("Coneccion establecida!.")
        except (OSError, comtypes.COMError):
            print("Cannot start a new instance of the program.")
            sys.exit(-1)
    print("Ejecutando!.")
    #start ETABS application | ejecutar la Aplicacion ETABS.
    connect_to_app.ApplicationStart()

smodel = connect_to_app.SapModel;


#initialize model
smodel.InitializeNewModel()

#create new blank model
response = smodel.File.NewBlank()

#define material property
MATERIAL_CONCRETE = 1
response = smodel.PropMaterial.SetMaterial('Other', MATERIAL_CONCRETE)

#assign isotropic mechanical properties to material
mod_e = 10000
response = smodel.PropMaterial.SetMPIsotropic('Other', mod_e, 0.2, 0.0000055)

#define rectangular frame section property
area = np.sqrt(0.111)
response = smodel.PropFrame.SetRectangle('R1', 'Other', area, area)

#define frame section property modifiers
ModValue = [1, 1, 1, 1, 1, 1, 1, 1]
response = smodel.PropFrame.SetModifiers('R1', ModValue)

#switch to k-ft units
kip_ft_F = 3
response = smodel.SetPresentUnits(kip_ft_F)

# Vertices o coordenadas
for i in range(nn):
    response = smodel.PointObj.AddCartesian(nodes[i,0], nodes[i,1], nodes[i,2], str(i+1))

# elementos o  miembros
FrameName1 = ' '
for i in range(ne):
    [FrameName1, ret] = smodel.FrameObj.AddByPoint(str(elems[i,0]+1), str(elems[i,1]+1), 'FrameName'+str(i+1), 'R1')
    # print([FrameName1, ret], (str(elems[i,0]+1), str(elems[i,1]+1), 'FrameName'+str(i+1), 'R1') )

#assign point object restraint at base
Restraint = [True, True, True, True, False, False]
response = smodel.PointObj.SetRestraint('7', Restraint)
response = smodel.PointObj.SetRestraint('8', Restraint)
response = smodel.PointObj.SetRestraint('9', Restraint)
response = smodel.PointObj.SetRestraint('10', Restraint)

#assign frame object release
Restraint_ii = [True, True, False, False, False, False]
Restraint_jj = [True, True, False, False, False, False]
StartValues = [0,0,0,0,0,0]
EndValues = [0,0,0,0,0,0]
for i in range(25):
    response = smodel.FrameObj.SetReleases(str(i+1), Restraint_ii, Restraint_jj, StartValues, EndValues)

#refresh view, update (initialize) zoom
response = smodel.View.RefreshView(0, False)

#add load patterns
LTYPE = 8
response = smodel.LoadPatterns.Add('1', LTYPE, 0, True)

#assign loading for load pattern 1
PointLoadValue = [1,-10,-10,0,0,0]
response = smodel.PointObj.SetLoadForce('1', '1', PointLoadValue)
#assign loading for load pattern 2
PointLoadValue = [0,-10,-10,0,0,0]
response = smodel.PointObj.SetLoadForce('2', '1', PointLoadValue)
#assign loading for load pattern 3
PointLoadValue = [0.5,0,0,0,0,0]
response = smodel.PointObj.SetLoadForce('3', '1', PointLoadValue)
#assign loading for load pattern 4
PointLoadValue = [0.6,0,0,0,0,0]
response = smodel.PointObj.SetLoadForce('6', '1', PointLoadValue)

#full path to the model, set it to the desired path of your model
APIPath = 'C:\\CSiAPI_Examples'
if not os.path.exists(APIPath):
    try: os.makedirs(APIPath)
    except OSError: pass
ModelPath = APIPath + os.sep + 'API_1-001.sdb'
#save model
response = smodel.File.Save(ModelPath)

#run model (this will create the analysis model)
response = smodel.Analyze.RunAnalysis()


#initialize for results
Axial = np.zeros(25)
Reactions = np.zeros([4,3])
Displacement = np.zeros([10,3])

response = smodel.Results.Setup.DeselectAllCasesAndCombosForOutput()
response = smodel.Results.Setup.SetCaseSelectedForOutput('1')

NumberResults = 0
Obj = []
Elm = []
ACase = []
StepType = []
StepNum = []
ObjectElm = 0
ObjSta = []
ElmSta = []
P = []
V2, V3 = [], []
T = []
M2, M3 = [], []
Element = 1
F1, F2, F3 = [], [], []
R1, R2, R3 = [], [], []
GroupElm = 2
U1, U2, U3, U4, U5, U6 = [], [], [], [], [], []
# get results for load cases 1 through 7
# optener resultados para los casos de carga 1 a 7
for i in range(ne):
    [NumberResults, Obj, ObjSta, ELm, ElmSta, ACase, StepType, StepNum, P, V2, V3, T, M2, M3, response] = \
    smodel.Results.FrameForce(str(i+1), ObjectElm, NumberResults, Obj, ObjSta, Elm, ElmSta, ACase, StepType, StepNum, P, V2, V3, T, M2, M3)
    Axial[i]=P[0]
for i in range(4):
    [NumberResults, Obj, Elm, ACase, StepType, StepNum, F1, F2, F3, R1, R2, R3, response] = \
    smodel.Results.JointReact(str(i+7), Element, NumberResults, Obj, Elm, ACase, StepType, StepNum, F1, F2, R1, R2, R3)
    Reactions[i,0] = F1[0]
    Reactions[i,1] = F2[0]
    Reactions[i,2] = F3[0]
for i in range(nn):
    [NumberResults, Obj, Elm, ACase, StepType, StepNum, U1,U2,U3,U4,U5,U6, response] = \
    smodel.Results.JointDispl(str(i+1), Element, NumberResults, Obj, Elm, ACase, StepType, StepNum, U1, U2, U3, U4, U5, U6)
    Displacement[i,0] = U1[0]
    Displacement[i,1] = U2[0]
    Displacement[i,2] = U3[0]

#close the program | cerrar
response = connect_to_app.ApplicationExit(False)
connect_to_app, smodel = None, None

#display results | mostra resultados
print(f"Axial Force\n{Axial[np.newaxis].T}")
print(f"Reaction forces\n{Reactions}")
print(f"Joint Displacement\n{Displacement}")

del connect_to_app, smodel, response
sys.exit()