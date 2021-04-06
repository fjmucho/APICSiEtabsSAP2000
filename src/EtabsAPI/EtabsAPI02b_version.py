#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
""" 
Para usar esta script tiene que estar ejecutandose Etabs.

Methods.: información
	comtypes.client
		.GetActiveObject(Progit, interface=None, dynamic=False)
		.SapModel
			.GetProgramInfo(param0, param1, param2)
			.GetVersion(param0, param1)
"""
import sys
import comtypes.client

# defininamos dos variables para optener la version de la aplicacion
version, myVersionNumber = "", 0.0
# definamos tres variables para nombrePrograma, versionPrograma, nivelPrograma.
nombrePrograma, versionPrograma, nivelPrograma = "", "", ""

try:
	# Connecting | coneccion
	ETABSObject = comtypes.client.GetActiveObject("CSI.ETABS.API.ETABSObject")
	print("Coneccion exitosa!.\nadjuntando a una instancia existente.")
except (OSError, comtypes.COMError):
	# No running instance of the program found or failed to attach.
	print("No se encontro ninguna instancia en ejecucion del programa(Etabs).")
	sys.exit(-1)

# create SapModel object | Crea el objeto Modelo
SapModel = ETABSObject.SapModel


fullNameEtabs = []
# Retrieve information about the program | ... informacion acerca del programa
fullNameEtabs = SapModel.GetProgramInfo()
nombrePrograma, versionPrograma, nivelPrograma = fullNameEtabs[0], fullNameEtabs[1], fullNameEtabs[2]
print(fullNameEtabs)

# get program version | Optener la version del Programa
retVersion = SapModel.GetVersion(version, myVersionNumber)
print(retVersion)


# Unlocking model | Mantener Cerrado modelo (hace referencia al candadito de etabs)
SapModel.SetModelIsLocked(True)

# clean up variables | limpiamos las variables y eliminamos
EtabsObject, SapModel, retVersion, fullNameEtabs= None, None, None, None
del version, myVersionNumber, nombrePrograma, versionPrograma, nivelPrograma # eleminamos las variables (objetos)
del EtabsObject, SapModel, retVersion, fullNameEtabs
# sys.exit(dir(ETABSObject.SapModel))

'''
['AddRef', 'Analyze', 
'AreaElm', 'AreaObj', 'BridgeAdvancedSuper', 'BridgeDesign', 'BridgeModeler', 
'BridgeObj', 'CableObj', 'ConstraintDef', 'CoordSys', 'DatabaseTables', 'DesignAluminum', 
'DesignColdFormed', 'DesignCompositeBeam', 'DesignConcrete', 'DesignConcreteSlab', 'DesignResults', 
'DesignShearWall', 'DesignSteel', 'Detailing', 'Diaphragm', 'EditArea', 'EditFrame', 'EditGeneral', 
'EditPoint', 'EditSolid', 'ExternalAnalysisResults', 
'File', 'FrameObj', 'Func', 'GDispl', 'GenRefLine', 
'GetDatabaseUnits', 'GetDatabaseUnits_2', 'GetIDsOfNames', 'GetKeyStringsExtendedEntityData', 
'GetKeysWithStringsExtendedEntityData', 'GetMergeTol', 'GetModelFilename', 'GetModelFilepath', 
'GetModelIsLocked', 'GetPresentCoordSystem', 'GetPresentUnits', 'GetPresentUnits_2', 'GetProgramInfo', 
'GetProjectInfo', 'GetTypeInfo', 'GetTypeInfoCount', 'GetUserComment', 'GetVersion', 'GridSys', 'GroupDef', 
'InitializeNewModel', 'Invoke', 'LineElm', 'LinkElm', 'LinkObj', 'LoadCases', 'LoadPatterns', 'NamedAssign', 
'NamedDisplay', 'NamedSet', 'Options', 'PatternDef', 'PierLabel', 'PlaneElm', 'PointElm', 'PointObj', 
'PropArea', 'PropAreaSpring', 'PropCable', 'PropFrame', 'PropLineSpring', 'PropLink', 'PropMaterial', 
'PropPointSpring', 'PropRebar', 'PropSolid', 'PropTendon', 'QueryInterface', 'Release', 'RespCombo', 
'Results', 'Scheduler', 'SectCut', 'SelectObj', 'SetMergeTol', 'SetModelIsLocked', 'SetPresentCoordSystem', 
'SetPresentUnits', 'SetPresentUnits_2', 'SetProjectInfo', 'SetStringsExtendedEntityData', 'SetUserComment', 
'SolidElm', 'SolidObj', 'SourceMass', 'SpandrelLabel', 'Story', 'TendonObj', 'Tower', 'TreeIsUpdateSuspended', 
'TreeResumeUpdateData', 'TreeSuspendUpdateData', 'View', 
...
'value']
'''