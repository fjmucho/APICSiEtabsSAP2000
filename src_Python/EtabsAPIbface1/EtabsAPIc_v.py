#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
""" 
información: Para usar esta script tiene que estar ejecutandose Etabs.

Methods.: 
	comtypes.client
		.GetActiveObject(Progit, interface=None, dynamic=False)
		.SapModel
			.GetProgramInfo(param0, param1, param2, param3)
			.GetVersion(p0, p1, p2)
Devuelve:
param0: string ProgramName
param1: string ProgramVersion
param2: string ProgramLevel
param3: int VersionNumberMayor
p0: string ProgramVersion
p1: double VersionNumber
p3: int VersionNumberMayor
"""
import sys
import comtypes.client

# defininamos dos variables para optener la version de la aplicacion
version, myVersionNumber, VersionNumberMayor = "", 0.0, 0
# definamos tres variables para nombrePrograma, versionPrograma, nivelPrograma.
nombrePrograma, versionPrograma, nivelPrograma = "", "", ""
EtabsObject=None
smodel=None

try:
	EtabsObject = comtypes.client.GetActiveObject("CSI.ETABS.API.ETABSObject")
	print("Coneccion exitosa!.\nadjuntando a una instancia existente.")
except (OSError, comtypes.COMError):
	print("No se encontro ninguna instancia en ejecucion del programa(Etabs).")
	sys.exit(-1)

# create SapModel object | Crea el objeto Modelo
smodel = EtabsObject.SapModel

fullNameEtabs = []
# Retrieve information about the program | ... informacion acerca del programa
fullNameEtabs = smodel.GetProgramInfo()
nombrePrograma, versionPrograma, nivelPrograma = fullNameEtabs[0], fullNameEtabs[1], fullNameEtabs[2]
print(fullNameEtabs[3])

# get program version | Optener la version del Programa
(version, myVersionNumber, VersionNumberMayor) = smodel.GetVersion()
print(myVersionNumber)



input("Enter para cerrar Etabs!")
# Close the program | Cerrar la aplicacion
EtabsObject.ApplicationExit(False)
print("Se ha cerrado la aplicación con Exito.")

# clean up variables | limpiamos las variables y eliminamos
EtabsObject, smodel, fullNameEtabs= None, None, None
version, myVersionNumber, nombrePrograma, versionPrograma, nivelPrograma = None, None, None, None, None
del version, myVersionNumber, nombrePrograma, versionPrograma, nivelPrograma # eleminamos las variables (objetos)
del EtabsObject, smodel, fullNameEtabs

# sys.exit(dir(ETABSObject.SapModel))