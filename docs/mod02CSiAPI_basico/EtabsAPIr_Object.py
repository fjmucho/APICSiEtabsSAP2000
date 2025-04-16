import comtypes.client


class EtabsProject():
    def __init__(self):
        try:
            ActiveObject = True
            myEtabsObject = comtypes.client.GetActiveObject('CSI.ETABS.API.ETABSObject')
            print('Açık bir Etabs projesi bulundu...')
        except:
            ActiveObject = False
            print('Yeni bir proje başlatılıyor...')
            myEtabsObject = comtypes.client.CreateObject('ETABSv1.Helper').QueryInterface(comtypes.gen.ETABSv1.cHelper).\
                CreateObjectProgID('CSI.ETABS.API.ETABSObject')
            myEtabsObject.ApplicationStart()

        finally:
            self.SapModel = myEtabsObject.SapModel
            if ActiveObject == False:
                self.SapModel.InitializeNewModel()

        # self.CreateGridSystem()
        # self.matNames()
        # self.getMatProp()
        # self.createNewMaterial()
        # self.deleteMaterial()
        # self.getSectName()
        # self.getSectProp()
        # self.createNewRectSect()
        # self.createNewSlab()
        self.getSlabProp()
        # self.deleteArea()
        self.getWallProp()
        self.createNewWall()

    def CreateGridSystem(self):
        self.SapModel.SetPresentUnits(6)
        self.SapModel.File.NewGridOnly(4, 3, 3, 4, 3, 3, 4)
        # self.SapModel.File.NewGridOnly(numberStory, typicalStoryHeight, BottomStoryHeight, numberLinesX, numberLinesY, SpacingX, SpacingY)


    def matNames(self):
        matName = self.SapModel.PropMaterial.GetNameList()
        print(matName)

    def getMatProp(self):
        getProp = self.SapModel.PropMaterial.GetOConcrete('C25/30')
        # GetOConcrete(Name, Fc, IsLightWeight, FcsFactor, SSType, SSHysType, StrainAtFc, StrainUltimate, FrictionAngle, DilatationAngle, temp)
        print(getProp)
        getWeight = self.SapModel.PropMaterial.GetWeightAndMass('C25/30')
        print(getWeight)
        getMechProp = self.SapModel.PropMaterial.GetMPIsotropic('C25/30')
        print(getMechProp)

    def createNewMaterial(self):
        self.SapModel.PropMaterial.SetMaterial('C30', 2)
        # SetOConcrete(Name, Fc, IsLightWeight, FcsFactor, SSType, SSHysType, StrainAtFc, StrainUltimate, FrictionAngle, DilatationAngle, temp)
        # Hognestad Method ==> StrainUltimate = 0.0038 ; Etabs StrainUltimate = 0.005
        # StrainAtFc = 2*Fc/E ==> 2 * 30 / 32000 = 0.001875
        self.SapModel.PropMaterial.SetOConcrete('C30', 30000, False, 0, 2, 4, 0.001875, 0.0038, 0, 0, 0)
        self.SapModel.PropMaterial.SetWeightAndMass('C30', 1, 25)
        self.SapModel.PropMaterial.SetMPIsotropic('C30', 32000000, 0.2, 1e-5)

    def deleteMaterial(self):
        self.SapModel.PropMaterial.Delete('C25/30')

    def getSectName(self):
        sectList = self.SapModel.PropFrame.GetNameList()
        print(sectList)

    def deleteSection(self):
        self.SapModel.PropFrame.Delete("ConcBm")

    def getSectProp(self):
        getProp = self.SapModel.PropFrame.GetRectangle('Column')
        print(getProp)
        getRebar = self.SapModel.PropFrame.GetRebarColumn('Column')
        print(getRebar)
        getModifiers = self.SapModel.PropFrame.GetModifiers('Column')
        print(getModifiers)

    def createNewRectSect(self):
        # self.SapModel.PropFrame.SetRectangle(Name, Material, Depth, Width, Color, Notes)
        # self.SapModel.PropFrame.SetRebarColumn(Name, LongRebarMaterial, ConfinRebarMaterial, Pattern, ConfineType, Cover, NumberCBars,
        # NumberR3Bars, NumberR2Bars, RebarSize, TieSize, TieSpacingLongit, Number2DirTieBars, Number3DirTieBars, ToBeDesigned)
        self.SapModel.PropFrame.SetRectangle('Kolon', 'C30', 1, 0.6, 264823, 'Bu ikinci bir kolon.')
        self.SapModel.PropFrame.SetRebarColumn('Kolon', 'Rebar', 'Rebar', 1, 0, 0.04, 0, 3, 5, '16', '12', 0.15, 4, 3, True)
        # self.SapModel.PropFrame.SetModifiers(Name, [KesitAlanı, Kesme_2, Kesme_3, Burulma, Moment_2, Moment_3, Kütle, Ağırlık])
        self.SapModel.PropFrame.SetModifiers('Kolon', [1.2, 0.8, 0.7, 0.90, 0.75, 0.75, 1.1, 0.75])

    def createNewSlab(self):
        # self.SapModel.PropArea.SetSlab('SlabName', 'SlabType', 'ShellType', 'Material', 'Thickness')
        self.SapModel.PropArea.SetSlab('d15', 0, 3, 'C30', 0.15)
        # slabModifiers = [f11, f22, f12, m11, m22, m12, v13, v22, mass, weight]
        slabModifiers = [1, 1, 1.2, 0.85, .9, 1.2, 1.25, 1, 1, 1]
        self.SapModel.PropArea.SetModifiers('d15', slabModifiers)

    def deleteArea(self):
        self.SapModel.PropArea.Delete('Plank1')

    def getSlabProp(self):
        areaNames = self.SapModel.PropArea.GetNameList()
        print(areaNames)
        slabProp = self.SapModel.PropArea.GetSlab('d15')
        print(slabProp)

    def getWallProp(self):
        wallProp = self.SapModel.PropArea.GetWall('Wall1')
        print(wallProp)

    def createNewWall(self):
        # self.SapModel.PropArea.SetWall('SlabName', 'WallType', 'ShellType', 'Material', 'Thickness')
        self.SapModel.PropArea.SetWall('W35', 1, 1, 'C30', .35)
        wallModifiers = [1.1, .9, 1.13, 0.85, .9, 1.2, 1.25, 1, 1, 1.5]
        self.SapModel.PropArea.SetModifiers('W35', wallModifiers)

EtabsProject()
