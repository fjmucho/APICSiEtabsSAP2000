#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""Description:
"""
import os, sys
import comtypes.client

try:
    ETABSObject = comtypes.client.GetActiveObject("CSI.ETABS.API.ETABSObject")
    print("Coneccion exitosa!.\nadjuntando a una instancia existente.")
except (OSError, comtypes.COMError):
    print("No se encontró ninguna instancia en ejecución del programa(Etabs).")
    sys.exit(-1)
    
SapModel = ETABSObject.SapModel
SapModel.SetModelIsLocked(False)
res = SapModel.InitializeNewModel()

# === FORMAS DE INICIALIZAR UN MODELO ===
# res = SapModel.File.NewBlank()
res = SapModel.File.NewGridOnly(4,12,12,4,4,24,24)
# res = SapModel.File.NewSteelDeck(4,12.0,12.0,4,4,24.0,24.0)

# Unit Preferences | Preferencias de Unidad
N_mm_C = 6 #kN_m_c
SapModel.SetPresentUnits(N_mm_C)


# recurso para optener las funciones que se tiene
for nombre in dir(SapModel.PropMaterial):
    if nombre.startswith('__') or nombre.startswith('_'):
        continue
    print(f"{nombre}")


# 'add ASTM A706 rebar material property in United states Region
ret = SapModel.PropMaterial.AddMaterial("CONC34", 2, "Spain", "HA-20", "Grade 60")
print(ret)

# Materials | materiales
SapModel.PropMaterial.SetMaterial("CONC35", 2, -1, "Comentario...")
mat_name_list=smodel.PropMaterial.GetNameList()
print(SapModel.PropMaterial.GetMaterial("CONC35"))
print(SapModel.PropMaterial.GetMaterial(mat_name_list[1][0]))

# 'change name of material property
ret = SapModel.PropMaterial.ChangeName("CONC35", "CONC36")


ret = SapModel.PropMaterial.SetOConcrete_1("CONC35", 35, False, 0, 1, 2, 0.0022, 0.0052, -0.1, 0, 0)
# 'assign other properties
ret = SapModel.PropMaterial.SetOConcrete("CONC37", 5, False, 0, 1, 2, 0.0022, 0.0052)

# 'specify temps at which properties will be provided
MyTemp = [0,50,100]
ret = SapModel.PropMaterial.SetTemp("Steel", 3, MyTemp)


input("Enter para cerrar Etabs!")
ETABSObject.ApplicationExit(True)

# clean up variables | limpiamos las variables y eliminamos
ETABSObject, SapModel, res = None, None, None
del ETABSObject, SapModel, res