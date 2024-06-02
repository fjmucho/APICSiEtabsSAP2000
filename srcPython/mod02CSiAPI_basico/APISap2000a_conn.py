import os, sys
import comtypes.client

def launcher():
    try:
        #trys to attach to a running instance
        mySapObject = comtypes.client.GetActiveObject("CSI.SAP2000.API.SapObject")
        SapModel = mySapObject.SapModel
        return mySapObject, _ # _=Sapmodel
    except OSError:
        #if no running instance, creates new instance
        print('os error')
        return False, False
        
def manually_launcher():
    helper = comtypes.client.CreateObject('SAP2000v19.Helper')
    helper = helper.QueryInterface(comtypes.gen.SAP2000v19.cHelper)
    ProgramPath = 'C:\\Program Files\\Computers and Structures\\SAP2000 23\\SAP2000.exe'
    mySapObject = helper.CreateObject(ProgramPath)
    mySapObject.ApplicationStart()
    smodel = mySapObject.SapModel
    smodel.File.NewBlank()
    return mySapObject, smodel

if __name__ == '__main__':
    a, b=launcher()
    print(a,b)