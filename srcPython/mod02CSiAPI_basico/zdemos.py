

import sys, os

def createDirectoryFile():
    #full path to the model, set it to the desired path of your model
    APIPath = 'C:\\CSi_API_Example'
    if not os.path.exists(APIPath):
        try:
            os.makedirs(APIPath) #| intenta crear un directorio.
        except OSError:
            print("Error: "+OSError) #| si no se tiene permiso laza un error.
    ModelPath = APIPath + os.sep + 'exampleAPI_1-001.edb'    
# prueba
createDirectoryFile()


import comtypes.client
def OpenFile():
    # 'open an existing file - If no file exists, run the Save example first.
    try:
        # fileName = APIPath = 'C:\\CSi_API_Example\\exAPI_1-001.edb'
        fileName = APIPath = 'C:\\CSi_API_Example\\API_1-001.$et'
    except (OSError, comtypes.COMError):
        print(f"No se puede abrir {comtypes.COMError}")
        sys.exit(-1)
# prueba
OpenFile()


# Para Validar programa ejecutable
def validar(ruta=""):
    print(ruta)
    ejecutable = ruta[-4:]
    if ejecutable==".exe":
        print(ejecutable)
        return True
    return False
texto = "C:\\Program Files\\Computers and Structures\\ETABS 21\\ETABS.exe"
validar(texto)