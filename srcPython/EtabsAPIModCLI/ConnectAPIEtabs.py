import comtypes.client

class ConnectAPIEtabs(object):
    def __init__(self): 
        try:
            #get the active ETABS object
            activeObject = True
            ETABSObject = comtypes.client.GetActiveObject("CSI.ETABS.API.ETABSObject")
            print("Coneccion exitosa!.\nadjuntando a una instancia existente.")
        except:
            activeObject == False
            # No running instance of the program found or failed to attach.
            print("No se encontró ninguna instancia en ejecución(Etabs).")
            # comtypes.client.CreateObject('ETABSv1.helper').QueryInterface(comtypes.gen.ETABSv1.cHelper).CreateObjectProID("CSI.ETABS.API.ETABSObject").ApplicationStart()
            ETABSObject = comtypes.client.CreateObject('ETABSv1.helper').\
                QueryInterface(comtypes.gen.ETABSv1.cHelper).\
                CreateObjectProgID("CSI.ETABS.API.ETABSObject")
            ETABSObject.ApplicationStart()
        finally:
            #create SapModel object | crea instancia del objeto SapModel
            self.smodel = ETABSObject.SapModel
            if activeObject == False:
                # 'initialize model | Inicializa una hoja en blanco para definir un modelo
                self.smodel.InitializeNewModel()
            else:
                # crea el lienzo vacio equivalente a figure en matplotlib
                # 'initialize model | Inicializa nuevo modelo en blanco
                self.smodel.InitializeNewModel()

        self.CreateGridSystem()

    def CreateGridSystem(self):
        self.smodel.SetPresentUnits(6)
        # create grid-only template model | Crea una nueva hoja con grilla
        # self.smodel.File.NewGridOnly(numberStory, typicalStoryHeight, BottomStoryHeigt, numberLinesX, numberLinesY, SpacingX, SpacingY)
        self.smodel.File.NewGridOnly(4,12,12,4,4,24,24)
    def matNames(self):
        matName = self.smodel.PropMaterial.GetNameList();
        print(matName)
    def getMatProp(self):
        getProp = self.smodel.PropMaterial.GetOConcrete('C25/30')
        # GetConcrete(Name, Fc, IsLightWeight, FcsFactor, SSType, SSHysType, StrainAtFo, StrainUltimate, FrctionAngle, DilatatonAngle, temp)
        print(getProp)
        getWeight = self.smodel.PropMaterial.GetWeightAndMass('C25/30')
        print(getWeight)
        getMechProp = self.smodel.PropMaterial.GetMPIsotropic('C25/30')
        print(getMechProp)
    def createNewMaterial(self):
        self.smodel.PropMaterial.SetMaterial('C30', 2)
        # SetOConcrete( Name, Fc, IsLightweight, FcsFactor, SSType, SSHysType, StrainAtFc, StrainUltimate, FrictionAngle, DilatationalAngle, Temp)
        # Hognestad Method ==> StrainUltimate = 0.0038; Etabs StrainUltimate = 0.005
        # StrainAtFc = 2*Fc/E ==> 2 * 30 / 32000 = 0.001875
        self.smodel.PropMaterial.SetOConcrete('C30', 30000, False, 0, 2, 4, 0.001875, 0.0038, 0, 0, 0)
        self.smodel.PropMaterial.SetWeightAndMass('C30', 1, 25)
        self.smodel.PropMaterial.SetMPIsotropic('C30', 32000000, 0.2, 1e-5)
    def deleteMaterial(self):
        self.smodel.PropMaterial.Delete('C25/30')
 
ConnectAPIEtabs()

print("La sesión actual de este programa se conectó haciendo uso de la API. \
Se recomenda que cierre este programa utilizando el programa desde el que se inició.")
input("Enter para cerrar Etabs!")
ETABSObject.ApplicationExit(False)
