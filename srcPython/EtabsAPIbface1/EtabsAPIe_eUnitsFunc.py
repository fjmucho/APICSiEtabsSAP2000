#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
**************** 0 ******************
@date: 06/04/21 to 20/04/21
@author: F. JMucho. <fjmucho0@gmail.com>
@Description: implelemntacion en una funcion
**************** 0 ****************** 
"""
unitOption = {
        'lb_in_F':1, 'lb_ft_F':2, 'kip_in_F':3, 'kip_ft_F':4, 'kN_mm_C':5, 
        'kN_m_C':6, 'kgf_mm_C':7, 'kgf_m_C':8, 'N_mm_C':9, 'N_m_C':10, 
        'Ton_mm_C':11, 'Ton_m_C':12, 'kN_cm_C':13, 'kgf_cm_C':14, 
        'N_cm_C':15, 'Ton_cm_C':16
    }

def add_eUnits(smodel=None, mi_unidad=""):
    # Unit Preferences | Preferencias de Unidad
    # N_mm_C = 6 #kN_m_c
    # smodel.SetPresentUnits(N_mm_C)
    
    unit_n_mm_n = mi_unidad #, propiedad estatica y deberia ser privada
    # su utilidad de estas 2 variables se usara para las funciones/metodos
    length="mm" # longitud
    force="kN"   #

    # length can be either "m" or "mm" 
    # force can be either "N" or "kN" 
    if(length=="mm" and force=="N"):
        # smodel.SetPresentUnits(9);
        smodel.SetPresentUnits(unit_n_mm_n);
    elif(length=="mm" and force=="kN"):
        # smodel.SetPresentUnits(5);
        smodel.SetPresentUnits(unit_n_mm_n);
    elif(length=="m" and force=="N"):
        # smodel.SetPresentUnits(10);
        smodel.SetPresentUnits(unit_n_mm_n);
    elif(length=="m" and force=="kN"):
        # smodel.SetPresentUnits(6);
        smodel.SetPresentUnits(unit_n_mm_n)
    # ....
    print(smodel.GetPresentUnits())

if __name__ == '__main__':
    import sys
    from EtabsAPIa_connfunc import connect_to_etabs
    on_status, eobj = False, None
    # evaluamos si ya tenemos la coneccion a etabs
    if on_status == False:
        # aquii aprendimos que la coneccion no se mantiene en el tiempo
        # es muy diferente a una base de datos que maniene la conecion 
        on_status, eobj = connect_to_etabs()
        if on_status==False: sys.exit(-1)

    # create SapModel object | Crea la instancia al objeto SapModel (Area de trabajo)
    smodel = eobj.SapModel
    smodel.SetModelIsLocked(False)
    
    # crea el lienzo vacio equivalente a figure en matplotlib
    # 'initialize model | Inicializa nuevo modelo en blanco
    smodel.InitializeNewModel()
    dbmodel = smodel.File.NewBlank()


    add_eUnits(smodel, unitOption['kN_m_C'])

    
    smodel.SetModelIsLocked(True)

    input("Enter para cerrar Etabs!")
    # Close the program | Cerrar la aplicacion
    eobj.ApplicationExit(False)

    smodel, eobj, on_status = None, None, None
    dbmodel = None
    del smodel, eobj, dbmodel, on_status
    sys.exit(-1)