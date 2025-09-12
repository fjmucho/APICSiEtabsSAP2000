import comtypes.client
import pandas as pd
import sys, numpy as np
from math import sqrt

class Modelo_ETABS:
    def __init__(self, units, Z, U, S, Rx, Ry, Tp, Tl, condition_x, condition_y, app):
        self.units = units
        self.Z = Z
        self.U = U
        self.S = S
        self.Rx = Rx
        self.Ry = Ry
        self.Tp = Tp
        self.Tl = Tl
        self.condition_x = condition_x
        self.condition_y = condition_y
        
        self.SapModel, self.ETABSObject, self.helper = self.Connect_app(app)
        
        self.Units(self.units)
        self.Load_Combinations()
        self.Response_Spectrum(self.Tp, self.Tl)
        self.Load_Cases(self.Z, self.U, self.S, self.Rx, self.Ry)
        self.Inelastic_Response(self.Rx, self.Ry, self.condition_x, self.condition_y)
        self.Seismic_weight()
        self.Sections()
        
    def Connect_app(self, connect_to=1):
        helper = comtypes.client.CreateObject('ETABSv1.Helper')
        helper = helper.QueryInterface(comtypes.gen.ETABSv1.cHelper)
        CSiObject = helper.GetObject("CSI.ETABS.API.ETABSObject")
        # CSiObject = helper.CreateObjectProgID("CSI.ETABS.API.ETABSObject")
        # CSiObject.ApplicationStart()
        SapModel = CSiObject.SapModel
        return SapModel, CSiObject, helper 
    
    def Units(self, units):
        # kgf_cm_C = 14
        self.SapModel.SetPresentUnits(units)

    def Concrete_material(self, fc):
        Conc_name = "fc = " + str(fc) + " kg/cm2"
        ret = self.SapModel.PropMaterial.SetMaterial(Conc_name, 2)
        ret = self.SapModel.PropMaterial.SetOConcrete_1(Conc_name, fc, False, 0, 1, 2, 0.0022, 0.0052, -0.1, 0, 0)
        ret = self.SapModel.PropMaterial.SetMPIsotropic(Conc_name, 15100*sqrt(fc), 0.2, 0.0000099)
        return Conc_name
    
    def Rebar_material(self, fy):
        Rebar_name = "fy = " + str(fy) + " kg/cm2"
        ret = self.SapModel.PropMaterial.SetMaterial(Rebar_name, 6)
        ret = self.SapModel.PropMaterial.SetORebar_1(Rebar_name, fy, 6300, fy, 6300, 2, 2, 0.02, 0.1, -0.1, False)
        ret = self.SapModel.PropMaterial.SetMPIsotropic(Rebar_name, 2*(10**6), 0.2, 0.0000117)
        return Rebar_name
    
    def Beams_section(self, b, h, fc, fy):
        Cname = self.Concrete_material(fc)
        Rname = self.Rebar_material(fy)
        ret = self.SapModel.PropFrame.SetRectangle('V'+str(b)+'x'+str(h), Cname, h, b)
        ret = self.SapModel.PropFrame.SetRebarBeam('V'+str(b)+'x'+str(h), Rname, Rname, 0, 0, 0, 0, 0, 0)
    
    def Columns_section(self, b, h, fc, fy):
        Cname = self.Concrete_material(fc)
        Rname = self.Rebar_material(fy)
        ret = self.SapModel.PropFrame.SetRectangle('C'+str(b)+'x'+str(h), Cname, h, b)
        ret = self.SapModel.PropFrame.SetRebarColumn('C'+str(b)+'x'+str(h), Rname, Rname, 2, 2, 2, 10, 0, 0, "#10", "#5", 4, 0, 0, False)
    
    def Load_Combinations(self):
        # Dataframe de las cargas creadas con las combinaciones consideradas
        data = {
            'Load Cases' :                  ["Peso Propio", "CM", "CV", "SExx", "SEyy"],      # Load Patterns
            'C1 = 1.4CM + 1.7CV' :          [1.40, 1.40, 1.70, 0, 0],                         # Combination
            'C2 = 1.25(CM + CV) + SExx':    [1.25, 1.25, 1.25, 1, 0],                         # Combination
            'C3 = 1.25(CM + CV) + SEyy':    [1.25, 1.25, 1.25, 0, 1],                         # Combination
            'C4 = 0.9CM + SExx':            [0.90, 0.90, 0.00, 1, 0],                         # Combination
            'C5 = 0.9CM + SEyy':            [0.90, 0.90, 0.00, 0, 1],                         # Combination
            'P = CM + 25%CV':               [1.00, 1.00, 0.25, 0, 0]                          # Combination
        }
        df = pd.DataFrame(data = data)
        (x, y) = df.shape
        
        # Definición del tipo de carga y el multiplicador
        ret = self.SapModel.LoadPatterns.Add(df.loc[0,'Load Cases'], 1, 1)     # Peso Propio
        ret = self.SapModel.LoadPatterns.Add(df.loc[1,'Load Cases'], 1, 0)     # Carga muerta
        ret = self.SapModel.LoadPatterns.Add(df.loc[2,'Load Cases'], 3, 0)     # Carga viva
        ret = self.SapModel.LoadPatterns.Add(df.loc[3,'Load Cases'], 5, 0)     # Sismo estático en X
        ret = self.SapModel.LoadPatterns.Add(df.loc[4,'Load Cases'], 5, 0)     # Sismo estático en Y

        # Creación de las combinaciones de carga en base al DataFrame
        for i in range(y-1):
            ret = self.SapModel.RespCombo.Add(df.columns.values[i+1], 0)
            for j in range (x):
                if df.loc[j, df.columns.values[i+1]] == 0:
                    continue       
                else:
                    ret = self.SapModel.RespCombo.SetCaseList(df.columns.values[i+1], 0, df.loc[j,'Load Cases'], df.loc[j,df.columns.values[i+1]])
    
    def Response_Spectrum(self, Tp, Tl):
        T = []; C = []
        for t in np.arange(0, Tl+5, 0.01):
            if t <= Tp:         Cs = 2.5
            elif Tp < t <= Tl:  Cs = 2.5*Tp/t
            else:               Cs = 2.5*(Tp*Tl)/(t**2)
            T.append(t)
            C.append(Cs)
        df = pd.DataFrame({'T' : T, 'C' : C})
        df.to_csv('ESPECTRO_XY.txt', header=None, index=None, sep='\t')
        
    def Load_Cases(self, Z, U, S, Rx, Ry):
        # Creación de los Load Cases
        ret = self.SapModel.LoadCases.ResponseSpectrum.SetCase('DinXX')
        ret = self.SapModel.LoadCases.ResponseSpectrum.SetCase('DinYY')

        # Asignación de espectro de respuesta a los Load Cases
        ret = self.SapModel.LoadCases.ResponseSpectrum.SetLoads('DinXX', 1, ['U1'], ['ESPECTRO_XY'], [(Z*U*S/Rx)*9.81], ['Global'], [0])
        ret = self.SapModel.LoadCases.ResponseSpectrum.SetLoads('DinYY', 1, ['U2'], ['ESPECTRO_XY'], [(Z*U*S/Ry)*9.81], ['Global'], [0])
    
    def Inelastic_Response(self, Rx, Ry, condition_x, condition_y):
        # Verificacion de irregularidad - Eje X
        if condition_x == 'Regular':          factor_x = 0.75
        elif condition_x == 'Irregular':      factor_x = 0.85
        
        # Verificacion de irregularidad - Eje Y
        if condition_y == 'Regular':          factor_y = 0.75
        elif condition_y == 'Irregular':      factor_y = 0.85

        # Creacion de combinacion de cargas de respuestas inelásticas
        ret = self.SapModel.RespCombo.Add('RIX', 0)
        ret = self.SapModel.RespCombo.Add('RIY', 0)
        ret = self.SapModel.RespCombo.SetCaseList('RIX', 0, 'DinXX', factor_x*Rx)
        ret = self.SapModel.RespCombo.SetCaseList('RIY', 0, 'DinYY', factor_y*Ry)
    
    def Seismic_weight(self):
        ret = self.SapModel.PropMaterial.SetMassSource_1(True, False, True, 1, ["CM", "CV"], [1.00, 0.25])
        
    def Sections(self):
        data = pd.read_excel('data/Secciones.xlsx')
        for _, row in data.iterrows():
            if row['Tipo'] == 'Viga':       self.Beams_section(row['b'], row['h'], row['fc'], row['fy'])
            elif row['Tipo'] == 'Columna':  self.Columns_section(row['b'], row['h'], row['fc'], row['fy'])