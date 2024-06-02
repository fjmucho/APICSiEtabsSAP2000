#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
**************** 0 ******************
@date: 06/04/21 to 20/04/21
@author: F. JMucho. <fjmucho0@gmail.com>
@Description: implelemntacion en una funcion
**************** 0 ****************** 
"""
def get_version_etabs(smodel=None):
    
    full_version_etabs = []
    etabs_version = []
    # Retrieve information about the program | ... informacion acerca del programa
    full_version_etabs = smodel.GetProgramInfo()
    # print(full_version_etabs)

    etabs_version = smodel.GetVersion()
    print(etabs_version)

    return full_version_etabs


if __name__ == '__main__':
    import sys
    from EtabsAPIa_connfunc import connect_to_etabs
    on_status, EtabsObject, smodel = False, None, None
    on_status, EtabsObject = connect_to_etabs()
    if on_status==False: exit()

    # create SapModel object | Crea la instancia al objeto SapModel (Area de trabajo)
    smodel = EtabsObject.SapModel

    etabsv = []
    etabsv = get_version_etabs(smodel)
    print(etabsv)

    on_status, EtabsObject, smodel = None, None, None
    etabsv = None
    del smodel, EtabsObject, on_status, etabsv
    sys.exit(-1)