#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
**************** 0 ******************
@date: 06/04/21
@author: F. JMucho. <fjmucho0@gmail.com>
@Description:
**************** 0 ******************
"""
# establecer o agregar materiales
def add_conc_materials(smodel, delete_existing=False):
    """
    This will set all the concrete grades with material properties to AS3600,
    20,25,32,40,50,60,65,70,80,100. The materials will have the designation
    'Conc-40' etc
    
    Parameters
    SapModel (smodel) : Pointer (refer to function connect_to_etabs)
    delete_existing : Boolean. If True will delete all existing concrete 
                      materials
    
    Returns None
    """
    conc_mat_to_del=[];
    #Get existing concrete materials to be deleted
    if(delete_existing==True):
        mat_name_list=smodel.PropMaterial.GetNameList()
        all_materials=mat_name_list# get_all_materials(smodel);
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
        new_prop=smodel.PropMaterial.AddMaterial(conc_nm,2,"User","AS3600",
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
    return None;

# optener materiales definidos
def get_materials():
    passs