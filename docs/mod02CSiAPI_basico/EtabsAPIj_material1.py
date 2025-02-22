#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""Description:

"""
import os
import sys
import comtypes.client

try:
    ETABSObject = comtypes.client.GetActiveObject("CSI.ETABS.API.ETABSObject")
    print("Coneccion exitosa!.\nadjuntando a una instancia existente.")
except (OSError, comtypes.COMError):
    print("No se encontró ninguna instancia en ejecución del programa(Etabs).")
    sys.exit(-1)
smodel = ETABSObject.SapModel()
smodel.SetModelIsLocked(False)
res = smodel.InitializeNewModel()

res = smodel.File.NewGridOnly(4,12,12,4,4,24,24)

# Unit Preferences | Preferencias de Unidad
N_mm_C = 6 #kN_m_c
smodel.SetPresentUnits(N_mm_C)

delete_existing=False

conc_mat_to_del=[];
#Get existing concrete materials to be deleted
if(delete_existing==True):
    all_materials=get_all_materials(smodel);
    for mat in all_materials:
        if(all_materials[mat]['mat_type']=='Concrete'):
            conc_mat_to_del+=[mat];
conc_grade=[25,32,40,50,65,80,100];
#Delete materials
for mat in conc_mat_to_del:
    prop_del=smodel.PropMaterial.Delete(mat);
    if(prop_del==1): 
        print('Deleting material {} unsuccessful'.format(mat));
for grade in conc_grade:
    conc_nm="CONC-"+str(grade);
    new_prop=smodel.PropMaterial.AddMaterial(conc_nm,
                                            2,
                                            "User","AS3600",
                                            str(grade)+'MPa',
                                            UserName=conc_nm);
    isLightweight=False;
    fcsFact=0.0;
    SSType=2;
    SSHysType=4;
    strainAtFc=0.003;
    strainAtUlt=0.0035;
    smodel.PropMaterial.SetOConcrete(conc_nm,grade,isLightweight,fcsFact,
                                        SSType,SSHysType,strainAtFc,
                                        strainAtUlt)
    conc_E={25:26700,
            32:30100,
            40:32800,
            50:34800,
            65:37400,
            80:39600,
            100:42200};
    concU=0.2
    concA=10*10**-6
    smodel.PropMaterial.SetMPIsotropic(conc_nm,conc_E[grade],concU,concA);
    smodel.PropMaterial.SetWeightAndMass(conc_nm,1,24.6*10**-6)

mat_name_list=smodel.PropMaterial.GetNameList();
print(mat_name_list)
print(len(mat_name_list))


input("Enter para cerrar Etabs!")
ETABSObject.ApplicationExit(True)

# clean up variables | limpiamos las variables y eliminamos
ETABSObject, smodel, res, mat_name_list = None, None, None, None
del ETABSObject, smodel, res, mat_name_list
