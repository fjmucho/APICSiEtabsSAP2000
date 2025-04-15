import comtypes.client
import sys

class ConnectCSiAPI(object):
    conn = {};
    # metodo contructor
    def __init__(self, connect_to):
        helper = comtypes.client.CreateObject('ETABSv1.Helper')
        helper = helper.QueryInterface(comtypes.gen.ETABSv1.cHelper)
        conection = select_app();

    @property
    def select_app(self):
        if connect_to == 1:  # SAP2000
            app_csi = "SAP2000"
            self.conn = {
                'app_ruta': "C:\\Program Files\\Computers and Structures\\SAP2000 23\\SAP2000.exe",
                'app_adjunto': "CSI.SAP2000.API.SapObject",
                'app_helper': 'SAP2000v1.Helper'
                }
        elif (connect_to == 2): # ETABS
            app_csi = "ETABS"
            self.conn = {
                'app_ruta': "C:\\Program Files\\Computers and Structures\\ETABS 21\\ETABS.exe",
                'app_adjunto': "CSI.ETABS.API.ETABSObject",
                'app_helper': "ETABSv1.Helper"
                }
        else: 
            print("No tenemos soporte aun")
            sys.exit()

    def not_connect(self): 
        print("No se pudo conectar...")
        sys.exit(-1)

    def connect_manually_to_etabs(self, ruta_programa=""):
        print("Tratando de Ejecutar etabs!.")
        
        on_status = False
        ETABSObject = None
        try:
            ETABSObject = helper.CreateObject(ruta_programa)
            print("Conexion esitosa!.\nConexion Manual establecida")
        except (OSError, comtypes.COMError):
            print("Cannot start a new instance of the program from " + ruta_programa)
            return False, ETABSObject
        print("Ejecutando etabs!.")
        ETABSObject.ApplicationStart()
        return True, ETABSObject
    
    def connect_default_to_etabs(self):
        print("Tratando de Ejecutar etabs!.")
        helper = comtypes.client.CreateObject('ETABSv1.Helper')
        helper = helper.QueryInterface(comtypes.gen.ETABSv1.cHelper)
        ETABSObject = None
        try:
            ETABSObject = helper.CreateObjectProgID("CSI.ETABS.API.ETABSObject") 
            print("Coneccion exitosa!.")
        except (OSError, comtypes.COMError):
            print(f"Cannot start a new instance of the program(etabs).")
            return False, ETABSObject
        print("Ejecutando etabs!.")
        ETABSObject.ApplicationStart()
        return True, ETABSObject
    
    def attach_to_instance():
        """ coneccion a etabs """
        on_status = False
        ETABSObject = None
        try:
            ETABSObject = comtypes.client.GetActiveObject("CSI.ETABS.API.ETABSObject") 
            print("Coneccion exitosa!.\nadjuntando a una instancia existente.")
            on_status = True
        except (OSError, comtypes.COMError):
            print("No se encontró ninguna instancia en ejecución del programa(etabs).")
        return on_status, ETABSObject, # _=smodel

        # try:
        #     #get the active ETABS object
        #     activeObject = True
        #     ETABSObject = comtypes.client.GetActiveObject("CSI.ETABS.API.ETABSObject")
        #     print("Coneccion exitosa!.\nadjuntando a una instancia existente.")
        # except:
        #     activeObject == False
        #     # No running instance of the program found or failed to attach.
        #     print("No se encontró ninguna instancia en ejecución(Etabs).")
        #     # comtypes.client.CreateObject('ETABSv1.helper').QueryInterface(comtypes.gen.ETABSv1.cHelper).CreateObjectProID("CSI.ETABS.API.ETABSObject").ApplicationStart()
        #     ETABSObject = comtypes.client.CreateObject('ETABSv1.helper').\
        #         QueryInterface(comtypes.gen.ETABSv1.cHelper).\
        #         CreateObjectProgID("CSI.ETABS.API.ETABSObject")
        #     ETABSObject.ApplicationStart()
        # finally:
        #     #create SapModel object | crea instancia del objeto SapModel
        #     self.smodel = ETABSObject.SapModel
        #     if activeObject == False:
        #         # 'initialize model | Inicializa una hoja en blanco para definir un modelo
        #         self.smodel.InitializeNewModel()
        #     else:
        #         # crea el lienzo vacio equivalente a figure en matplotlib
        #         # 'initialize model | Inicializa nuevo modelo en blanco
        #         self.smodel.InitializeNewModel()