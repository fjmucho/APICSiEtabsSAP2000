#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Autor: F. JMucho. <fjmucho0@gmail.com>
"""
import os;
import sys;
import comtypes.client;

def connect_to_etabs():
    """
    Return Values:
    SapModel (type cOAPI pointer)
    EtabsObject (type cOAPI pointer)
    """
    #attach to a running instance of ETABS
    try:
        #get the active ETABS object
        EtabsObject = comtypes.client.GetActiveObject("CSI.ETABS.API.ETABSObject")
    except (OSError,comtypes.COMError):
        print("No running instance of the program found or failed to attach.")
        sys.exit(-1)
    #create SapModel object
    SapModel=EtabsObject.SapModel
    #setEtabsUnits()
    return SapModel, EtabsObject

def get_story_data(smodel=None):
    """
    returns:
    story_data (list). The is a nested list with each element consists of
    [story_nm,story_ele,story_hgt,is_master_story,similar_to,splice_above,splice_height]
    """
    #Get the data using API
    #Separate the data to lists
    # story_in = smodel.Story.GetStories()
    # print(story_in) # tupla ...
    # print(story_in[8]) # no puedo optener el color por alguna razon me devuelve 0
    # print(len(story_in)) # ademas siempre devuelve 9, porque solo contamos con 9 campos en etabs
    nos_stories = 0 #NumberStories
    story_nms = [] #StoryNames
    story_eles = [] #StoryElevations
    story_hgts = [] #StoryHeights
    is_master_story = [] #IsMasterStory
    similar_to_story = [] #SimilarToStory
    splice_above = [] #SpliceAbove
    splice_height=[] #SpliceHeight
    color=0.0
    (nos_stories, story_nms, story_eles, story_hgts, is_master_story, similar_to_story, splice_above, splice_height,color)=smodel.Story.GetStories(
        nos_stories, story_nms, story_eles, story_hgts, 
        is_master_story, similar_to_story, splice_above, splice_height)

    #Combine data into one list called story_data
    story_data=[];
    for i in range(len(story_nms)):
        j=-1-i;
        story_data.append([story_nms[j],
                           round(story_hgts[j],3),
                           round(story_eles[j],3),
                           is_master_story[j],
                           similar_to_story[j],
                           splice_above[j],
                           splice_height[j]]);
    return story_data;

def set_etabs_units(smodel=None,length="mm",force="N"):
    """
    length can be either "m" or "mm"
    force can be either "N" or "kN"
    """
    if(length=="mm" and force=="N"): smodel.SetPresentUnits(9);
    elif(length=="mm" and force=="kN"): smodel.SetPresentUnits(5);
    elif(length=="m" and force=="N"): smodel.SetPresentUnits(10);
    elif(length=="m" and force=="kN"): smodel.SetPresentUnits(6);
    return None;

def get_all_frames(smodel=None):
    """
    Parameters:
    SapModel : SapModel.Pointer
    
    Returns:
    A list of frame elements in current Etabs model
    
    frames : list
    """
    frame_objs=smodel.FrameObj.GetAllFrames();
    # print(frame_objs[7]) # acesando a los campos
    # print(len(frame_objs)) # siempre me devuelve 21 datos
    #Initiate the frames list
    frames=[];
    #Populate the frames list with data from frame_objs
    for i in range(frame_objs[0]):
        frameNm=frame_objs[1][i];
        prop=frame_objs[2][i];
        story=frame_objs[3][i];
        pt1=frame_objs[4][i];
        pt2=frame_objs[5][i];
        x1=frame_objs[6][i];
        y1=frame_objs[7][i];
        z1=frame_objs[8][i];
        x2=frame_objs[9][i];
        y2=frame_objs[10][i];
        z2=frame_objs[11][i];
        rot=frame_objs[12][i];
        offX1=frame_objs[13][i];
        offY1=frame_objs[14][i];
        offZ1=frame_objs[15][i];
        offX2=frame_objs[16][i];
        offY2=frame_objs[17][i];
        offZ2=frame_objs[18][i];
        cardPt=frame_objs[19][i];
        frames+=[[frameNm,prop,story,
                  pt1,pt2,
                  x1,y1,z1,
                  x2,y2,z2,
                  rot,
                  offX1,offY1,offZ1,
                  offX2,offY2,offZ2,
                  cardPt]];
    return frames;

def get_all_materials(smodel=None):
    """
    Gets the materials in the current model. Will return in units mm, N & MPa.
    
    If the property type is either 'Concrete' or 'Steel', the function will
    be expanded so that the strength of materials are included.
    
    Returns
    materials : Type dict
    """
    # Set the Etabs units, all strength of materials will be returned in MPa
    smodel.SetPresentUnits(9);
    # Etabs material type enumerators
    mat_types={1:'Steel',2:'Concrete',3:'NoDesign',4:'Aluminum',5:'ColdFormed',
               6:'Rebar',7:'Tendon',8:'Masonry'}; 
    mat_name_list=smodel.PropMaterial.GetNameList();
    # print(mat_name_list)
    # print()
    materials={};
    for i in range(mat_name_list[0]):
        mat_name=mat_name_list[1][i];
        mat_props=smodel.PropMaterial.GetMaterial(mat_name);
        mat_type=mat_types[mat_props[0]];
        if(mat_type=='Concrete'):
            mat_conc_prop=smodel.PropMaterial.GetOConcrete_1(mat_name);
            conc_fc=mat_conc_prop[0];
            materials[mat_name]={'mat_name':mat_name,'mat_type':mat_type,
                                 'fc':conc_fc};
        elif(mat_type=='Steel'):
            mat_steel_prop=smodel.PropMaterial.GetOSteel_1(mat_name);
            steel_fy=mat_steel_prop[0];
            steel_fu=mat_steel_prop[1];
            materials[mat_name]={'mat_name':mat_name,'mat_type':mat_type,
                                 'fy':steel_fy,'fu':steel_fu};
        else:
            materials[mat_name]={'mat_name':mat_name,'mat_type':mat_type};
    return materials;

def get_all_points(smodel=None, inc_restraint=True):
    """
    This will return all the points of the model.
    
    Parameters:
    SapModel : SapModel.Pointer
    inc_restraint : boolean (set True for restraints to be included
                             to points list)
    units : str. Default to 'mm'
    
    Returns:
    points : list (Points in current Etabs model). Elements in the points
    list if inc_restraint==False [pt_nm,x,y,z]. If inc_restraint==True the
    point element = [pt_nm,x,y,z,(FUx,FUy,FUz,FRx,FRy,FRz)]
    """
    [numberPts,ptNames,ptX,ptY,ptZ,ptCsys] = smodel.PointObj.GetAllPoints();
    #initiate a temporary list to contain the restrained points data
    ptsRestraint=[];
    if(inc_restraint==True):
        for i in range(numberPts):
            ptRestraintSA=smodel.PointObj.GetRestraint(ptNames[i]);
            ptRestraint=ptRestraintSA[0];
            ptsRestraint.append(ptRestraint);
    #Initiate the points list
    points=[]
    for i in range(numberPts):
        if(inc_restraint==True):
            points.append([ptNames[i],ptX[i],ptY[i],ptZ[i],ptsRestraint[i]]);
        else:
            points.append([ptNames[i],ptX[i],ptY[i],ptZ[i]]);
    return points;