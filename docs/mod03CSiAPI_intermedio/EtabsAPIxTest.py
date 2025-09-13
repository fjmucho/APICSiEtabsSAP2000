#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Autor: F. JMucho. <fjmucho0@gmail.com>
"""

from EtabsAPIx_GetFunctions import connect_to_etabs, \
    get_story_data, get_all_frames, get_all_materials, get_all_points, set_etabs_units

import numpy as np

if __name__ == '__main__':
    
    smodel, eobj = connect_to_etabs()
    # print(dir(smodel))

    # 9 campos para definir el numero de pisos
    data = get_story_data(smodel)
    print(data)
    print(len(data))
    print(np.array(data)) # para dar formato al array usamos numpy

    # 
    # set_etabs_units(smodel, length="", forces="")

    # # 21 campos para definir el numero de frames
    # fms = get_all_frames(smodel)
    # print(fms)
    # print(len(fms))
    # print(np.array(fms))


    # todom = get_all_materials(smodel)
    # print(todom)

    # el numero de puntos
    # pts = get_all_points(smodel, True)
    # print(pts)
    # print(np.array(pts))
    # print(len(pts))

    smodel, eobj, pts = None, None, None
    del smodel, eobj, pts