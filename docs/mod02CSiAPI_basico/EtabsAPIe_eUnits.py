#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Description:
"""
import os, sys
import comtypes.client

try:
    ETABSObject = comtypes.client.GetActiveObject("CSI.ETABS.API.ETABSObject")
    print("Coneccion exitosa!.\nadjuntando a una instancia existente.")
except (OSError, comtypes.COMError):
    print("No se encontró ninguna instancia en ejecución del programa(Etabs).")
    sys.exit(-1)
smodel = ETABSObject.SapModel

# Unlocking model | Abriendo modelo (hace referencia al candadito de etabs)
smodel.SetModelIsLocked(False)

# 'initialize model | Inicializa nuevo modelo en blanco
res = smodel.InitializeNewModel()

# create grid-only template model | Crea una nueva hoja con grilla
res = smodel.File.NewGridOnly(4,12,12,4,4,24,24)


# Unit Preferences | Preferencias de Unidad
# N_mm_C = 6 #kN_m_c
# smodel.SetPresentUnits(N_mm_C)

unitOption = {
'lb_in_F':1, 'lb_ft_F':2, 'kip_in_F':3, 'kip_ft_F':4, 
'kN_mm_C':5, 'kN_m_C':6, 'kgf_mm_C':7, 'kgf_m_C':8, 'N_mm_C':9, 'N_m_C':10, 
'Ton_mm_C':11, 'Ton_m_C':12, 'kN_cm_C':13, 'kgf_cm_C':14, 'N_cm_C':15, 'Ton_cm_C':16
}
_n_mm_n = unitOption['kN_m_C'] #, propiedad estatica y privada, deberia ser
# su utilidad de estas 2 variables se usara para las funciones/metodos
length="mm" # longitud
force="kN"   #

# length can be either "m" or "mm" 
# force can be either "N" or "kN" 
if(length=="mm" and force=="N"):
    # smodel.SetPresentUnits(9);
    smodel.SetPresentUnits(_n_mm_n);
elif(length=="mm" and force=="kN"):
    # smodel.SetPresentUnits(5);
    smodel.SetPresentUnits(_n_mm_n);
elif(length=="m" and force=="N"):
    # smodel.SetPresentUnits(10);
    smodel.SetPresentUnits(_n_mm_n);
elif(length=="m" and force=="kN"):
    # smodel.SetPresentUnits(6);
    smodel.SetPresentUnits(_n_mm_n)
# ....
print(smodel.GetPresentUnits())


input("Enter para cerrar Etabs!")
# 'close ETABS | Cerrar aplicacion Etabs
ETABSObject.ApplicationExit(False)

# clean up variables | limpiamos las variables y eliminamos
ETABSObject, smodel, res = None, None, None
del ETABSObject, smodel, res