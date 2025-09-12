import comtypes.client
import sys

class ConnectCSiAPI(object):
    conn = {};
    app_csi = None;
    # metodo contructor
    def __init__(self, connect_to=1):

        self.connect_to = connect_to

        if connect_to == 1:  # SAP2000
            self.app_csi = "SAP2000"
            self.conn = {
                'app_adjunto': "CSI.SAP2000.API.SapObject",
                'app_helper': 'SAP2000v1.Helper'
                }
        elif (connect_to == 2): # ETABS
            self.app_csi = "ETABS"
            self.conn = {
                'app_adjunto': "CSI.ETABS.API.ETABSObject",
                'app_helper': "ETABSv1.Helper"
                }
        else: 
            print("No tenemos soporte aun")
            sys.exit()
        print(self.app_csi)

    def connect_default(self):
        connect_to_app = None;
        helper = comtypes.client.CreateObject(self.conn['app_helper'])
        if self.connect_to == 1: helper = helper.QueryInterface(comtypes.gen.SAP2000v1.cHelper)
        if self.connect_to == 2: helper = helper.QueryInterface(comtypes.gen.ETABSv1.cHelper);

        try:
            connect_to_app = helper.CreateObjectProgID(self.conn["app_adjunto"])
        except (OSError, comtypes.COMError):
            print(f"Cannot start a new instance of the program({self.app_csi}).")
            return (False, connect_to_app)
        
        print(f"Coneccion establecida para {self.app_csi}!.")
        return (True, connect_to_app)

    def connect_manually(self, ruta_programa=""):
        on_status = False
        connect_to_app = None;
        helper = comtypes.client.CreateObject(self.conn['app_helper'])
        if self.connect_to == 1: helper = helper.QueryInterface(comtypes.gen.SAP2000v1.cHelper)
        if self.connect_to == 2: helper = helper.QueryInterface(comtypes.gen.ETABSv1.cHelper);

        try:
            connect_to_app = helper.CreateObject(ruta_programa)
            on_status = True
            print("Conexion esitosa!.\nConexion Manual establecida")
        except (OSError, comtypes.COMError):
            print(f"Cannot start a new instance of the program from {ruta_programa}")
            return (on_status, connect_to_app)
        
        return (on_status, connect_to_app)
    
    def attach_to_instance(self):
        """
        coneccion a etabs
        """
        on_status = False
        connect_to_app = None;
        try:
            connect_to_app = comtypes.client.GetActiveObject("CSI.ETABS.API.ETABSObject") 
            print("Coneccion exitosa!.\nadjuntando a una instancia existente.")
            on_status = True
        except (OSError, comtypes.COMError):
            print("No se encontró ninguna instancia en ejecución del programa(etabs).")
        return (on_status, connect_to_app)
    
    def not_connect(self): 
        print("No se pudo conectar...")
        sys.exit(-1)