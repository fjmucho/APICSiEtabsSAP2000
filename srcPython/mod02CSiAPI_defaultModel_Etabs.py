#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
| ----------------------------------------------------------------------- 
| Default example. - ejecucion en API de CSi
| -----------------------------------------------------------------------
| ref: C:\\Program Files\\Computers and Structures\\ETABS 17\\CSI API ETABS v1.chm
|      youtube: ....
| author: fjmucho0@gmail.com
| date created: 04/02/2021 

1) Review of API notation

2) Setup:
    Connecting to running instance of ETABS
    Unit preferences
    Unlocking model

3)  Defining:
	Materials
	Sections
	Cases
	Combinations

4) Creating:
	Elements
	Assigning forces
	    Joint forces
	    Distributed forces
	Assigning restraints

5) Post Processing
	Running analysis
	Getting results
	    Selecting load combinations

"""

# Imports
import os
import sys
import ctypes
import comtypes.client

try:
	# Connecting | coneccion
	ETABSObject = comtypes.client.GetActiveObject("CSI.ETABS.API.ETABSObject")
	print("Coneccion exitosa!.\nAdjuntando a una instancia existente.")
except (OSError, comtypes.COMError):
    print("No se encontró ninguna instancia en ejecución del programa(Etabs).")
    sys.exit(-1)
    
SapModel = ETABSObject.SapModel

# Unlocking model | Abriendo modelo (hace referencia al candadito de etabs)
SapModel.SetModelIsLocked(False)

# Unit Preferences | Preferencias de Unidad
# kN_m_C = 6 #kN_m_C
N_mm_C = 6
SapModel.SetPresentUnits(N_mm_C)

# Materials | materiales
name_material="Conc35"
SapModel.PropMaterial.SetMaterial(name_material, 2)

SapModel.PropMaterial.SetOConcrete_1(name_material, 35, False, 0, 1, 2, 0.0022, 0.0052, -0.1, 0, 0)

# Sections | secciones
sectionName = 'ConcSection'
SapModel.PropFrame.SetRectangle(sectionName, name_material, 400, 400)

# Patterns | patrones
ret = SapModel.LoadPatterns.Add("LCASE1", 2)
print(ret)
ret = SapModel.LoadPatterns.Add("LCASE2", 3)

# Cases | casos de carga
ret = SapModel.LoadCases.StaticLinear.SetCase("LCASE1")
ret = SapModel.LoadCases.StaticLinear.SetCase("LCASE1")

# Combinations | combinaciones

ret = SapModel.RespCombo.Add("COMB1", 0)

CNameType = 0
ret = SapModel.RespCombo.SetCaseList("COMB1", CNameType, "LCASE1", 1.25)
ret = SapModel.RespCombo.SetCaseList("COMB1", CNameType, "LCASE2", 1.5)

NumberItems = 0
CNameType = []
CName = []
SF = []
SapModel.RespCombo.GetCaseList("COMB1", NumberItems, CNameType, CName, SF)

# Elements | elementos
FrameName1 = ' '
FrameName2 = ' '
FrameName3 = ' '
[FrameName1, ret] = SapModel.FrameObj.AddByCoord(0, 0, 0, 0, 0, 10, FrameName1, sectionName, '1', 'Global')
[FrameName2, ret] = SapModel.FrameObj.AddByCoord(0, 0, 10, 8, 0, 16, FrameName2, sectionName, '2', 'Global')
[FrameName3, ret] = SapModel.FrameObj.AddByCoord(-4, 0, 10, 0, 0, 10, FrameName3, sectionName, '3', 'Global')

# Assigning restraints
PointName1 = ' '
PointName2 = ' '
Restraint = [True, True, True, True, True, True]
[PointName1, PointName2, ret] = SapModel.FrameObj.GetPoints(FrameName1, PointName1, PointName2)
ret = SapModel.PointObj.SetRestraint(PointName1, Restraint)

# Joint forces | junta de fuerzas

Value = (100.0, 0.0, 0.0, 0.0, 0.0, 0.0)
Value2 = [0.0, 200.0, 0.0, 0.0, 0.0, 0.0]

ret = SapModel.PointObj.SetLoadForce("4", "LCASE1", Value, True, 'Global', 0)
ret = SapModel.PointObj.SetLoadForce('3', 'LCASE2', Value2, True, 'Global', 0)


# save model | guardar nuestro modelo
# ModelPath = "C:\\Users\\Kanwar Johal\\Desktop\\ReFrame\\tutorial3.edb"
ModelPath = 'C:\\CSi_ETABS_API_Example\\tutorial3.edb'
ret = SapModel.File.Save(ModelPath)


#run model (this will create the analysis model)
ret = SapModel.Analyze.RunAnalysis()

ctypes.windll.user32.MessageBoxW(0, f"Ejecucion terminado", "CSiAPI", 64)
if (ETABSObject.ApplicationExit(False)): print("ETABS, No se pudo cerrar")
else: print("Se cerro con exito.")

# deselect all cases and combos
ret = SapModel.Results.Setup.DeselectAllCasesAndCombosForOutput

# set combo selected for output
ret = SapModel.Results.Setup.SetComboSelectedForOutput("COMB1")

# Get frame forces
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

ret = SapModel.Results.FrameForce(FrameName1, ObjectElm, NumberResults, Obj, ObjSta, Elm, ElmSta, LoadCase, StepType, StepNum, P, V2, V3, T, M2, M3)
print(ret)

smodel = None
ETABSObject = None
del smodel, ETABSObject, ret
exit(-1)

