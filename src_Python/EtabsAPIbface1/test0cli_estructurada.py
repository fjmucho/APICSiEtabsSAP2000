#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Si no entiende este escript, no lo ejecute, porque lanzara una eception.
...
"""
import os, sys
import comtypes.client
# Variable para definir una instancia manual para Etabs.
rutaEspecifica = True

#if the above flag is set to True, specify the path to ETABS below
# si la bandera anterior se establece en True, entonces debe especificar la ruta a ETABS a continuación
ProgramPath = r"C:\\Program Files\\Computers and Structures\\ETABS 19\\ETABS.exe"

# ModelPath = r"C:\\CSi_ETABS_API_Example\\API_1-001.EDB")
# # save model | guardar nuestro modelo
# full path to the model, set it to the desired path of your model
# APIPath = 'C:\\CSi_ETABS_API_Example'
# if not os.path.exists(APIPath):
#     try:
#         os.makedirs(APIPath) #| intenta crear un directorio.
#     except OSError:
#         print("Error: "+OSError) #| si no se tiene permiso laza un error.
# ModelPath = APIPath + os.sep + 'API_1-001.edb'
# ret = SapModel.File.Save(ModelPath)
# # 'display the filename of the model
# print(SapModel.GetModelFilename())


helper = comtypes.client.CreateObject('ETABSv1.Helper')
helper = helper.QueryInterface(comtypes.gen.ETABSv1.cHelper)

#create API helper object
myETABSObject = helper.CreateObject(ProgramPath)

# start ETABS application | ejecutar la aplicacion Etabs
myETABSObject.ApplicationStart()
#create SapModel object
SapModel = myETABSObject.SapModel
#initialize model
ret = SapModel.InitializeNewModel()

#open an existing file
ret = SapModel.File.OpenFile(ModelPath)

#run model (this will create the analysis model)
ret = SapModel.Analyze.RunAnalysis()

spandrelresults=SapModel.AnalysisResults.SpandrelForce()
spandrelresults=SapModel.AnalysisResults.SpandrelForce(1,"Level 1","S1", "Dead","Left")


values = SapModel.DatabaseTables.GetAllTables