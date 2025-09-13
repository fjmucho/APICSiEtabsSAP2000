# 
import comtypes.client

class CSiAPI():
    def __init__(self):
        try:
            ActiveObject = True
            connect_to_apiCSi = comtypes.client.GetActiveObject('CSI.ETABS.API.ETABSObject')
            print('Instancia a Programa CSiEtabs abierto.')
        except:
            ActiveObject = False
            connect_to_apiCSi = comtypes.client\
                                .CreateObject('ETABSv1.Helper')\
                                .QueryInterface(comtypes.gen.ETABSv1.cHelper)\
                                .CreateObjectProgID('CSI.ETABS.API.ETABSObject')
            connect_to_apiCSi.ApplicationStart()
        finally:
            self.smodel = connect_to_apiCSi.SapModel
            if ActiveObject == False:
                self.smodel.InitializeNewModel()

        # self.CreateGridSystem()
        # self.matNames()
        # self.getMatProp()
        # self.createNewMaterial()
        # self.deleteMaterial()
        # self.getSectName()
        # self.getSectProp()
        self.createNewRectSect()


    def CreateGridSystem(self):
        self.smodel.SetPresentUnits(6)
        self.smodel.File.NewGridOnly(4, 3, 3, 4, 3, 3, 4)
        # self.smodel.File.NewGridOnly(numberStory, typicalStoryHeight, BottomStoryHeight, numberLinesX, numberLinesY, SpacingX, SpacingY)


    def matNames(self):
        matName = self.smodel.PropMaterial.GetNameList()
        print(matName)

    def getMatProp(self):
        getProp = self.smodel.PropMaterial.GetOConcrete('C25/30')
        # GetOConcrete(Name, Fc, IsLightWeight, FcsFactor, SSType, SSHysType, StrainAtFc, StrainUltimate, FrictionAngle, DilatationAngle, temp)
        print(getProp)
        getWeight = self.smodel.PropMaterial.GetWeightAndMass('C25/30')
        print(getWeight)
        getMechProp = self.smodel.PropMaterial.GetMPIsotropic('C25/30')
        print(getMechProp)

    def createNewMaterial(self):
        self.smodel.PropMaterial.SetMaterial('C30', 2)
        # SetOConcrete(Name, Fc, IsLightWeight, FcsFactor, SSType, SSHysType, StrainAtFc, StrainUltimate, FrictionAngle, DilatationAngle, temp)
        # Hognestad Method ==> StrainUltimate = 0.0038 ; Etabs StrainUltimate = 0.005
        # StrainAtFc = 2*Fc/E ==> 2 * 30 / 32000 = 0.001875
        self.smodel.PropMaterial.SetOConcrete('C30', 30000, False, 0, 2, 4, 0.001875, 0.0038, 0, 0, 0)
        self.smodel.PropMaterial.SetWeightAndMass('C30', 1, 25)
        self.smodel.PropMaterial.SetMPIsotropic('C30', 32000000, 0.2, 1e-5)

    def deleteMaterial(self):
        self.smodel.PropMaterial.Delete('C25/30')

    def getSectName(self):
        sectList = self.smodel.PropFrame.GetNameList()
        print(sectList)

    def deleteSection(self):
        self.smodel.PropFrame.Delete("ConcBm")

    def getSectProp(self):
        getProp = self.smodel.PropFrame.GetRectangle('Column')
        print(getProp)
        getRebar = self.smodel.PropFrame.GetRebarColumn('Column')
        print(getRebar)
        getModifiers = self.smodel.PropFrame.GetModifiers('Column')
        print(getModifiers)

    def createNewRectSect(self):
        # self.smodel.PropFrame.SetRectangle(Name, Material, Depth, Width, Color, Notes)
        # self.smodel.PropFrame.SetRebarColumn(Name, LongRebarMaterial, ConfinRebarMaterial, Pattern, ConfineType, Cover, NumberCBars,
        # NumberR3Bars, NumberR2Bars, RebarSize, TieSize, TieSpacingLongit, Number2DirTieBars, Number3DirTieBars, ToBeDesigned)
        self.smodel.PropFrame.SetRectangle('Kolon', 'C30', 1, 0.6, 264823, 'Bu ikinci bir kolon.')
        self.smodel.PropFrame.SetRebarColumn('Kolon', 'Rebar', 'Rebar', 1, 0, 0.04, 0, 3, 5, '16', '12', 0.15, 4, 3, True)
        # self.smodel.PropFrame.SetModifiers(Name, [KesitAlanı, Kesme_2, Kesme_3, Burulma, Moment_2, Moment_3, Kütle, Ağırlık])
        self.smodel.PropFrame.SetModifiers('Kolon', [1.2, 0.8, 0.7, 0.90, 0.75, 0.75, 1.1, 0.75])


CSiAPI()
