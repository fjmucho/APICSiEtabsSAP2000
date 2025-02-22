
import sys, comtypes.client

def conexion(connect_to=1):
    conn = {};
    if connect_to == 1:  # SAP2000
        name_app = "SAP2000"
        conn = {
            'app_ruta': "C:\\Program Files\\Computers and Structures\\SAP2000 23\\SAP2000.exe",
            'app_adjunto': "CSI.SAP2000.API.SapObject",
            'app_helper': 'SAP2000v1.Helper'
            }
    elif (connect_to == 2): # ETABS
        name_app = "ETABS"
        conn = {
            'app_ruta': "C:\\Program Files\\Computers and Structures\\ETABS 21\\ETABS.exe",
            'app_adjunto': "CSI.ETABS.API.ETABSObject",
            'app_helper': "ETABSv1.Helper"
            }
    else: 
        print("No tenemos soporte aun")
        sys.exit()

    try:
        connect_to_app = comtypes.client.GetActiveObject(conn["app_adjunto"])
        print(f"Instancia establecida (adjuntada) a {name_app}")
    except (OSError, comtypes.COMError):
        print("No running instance of the program found or failed to attach.")
        sys.exit(-1)
    
    return name_app, connect_to_app