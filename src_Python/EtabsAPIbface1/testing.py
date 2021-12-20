
import EtabsAPI02b_conectf as connect
import EtabsAPI05e_saveFilef as savef
import EtabsAPI06f_openFilef as openf

if __name__ == '__main__':
	smodel, etabsObj = connect.connect_to_etabs()
	# create SapModel object | Crea el objeto Modelo
	smodel = etabsObj.SapModel
	# Unlocking model | Mantener Cerrado modelo (hace referencia al candadito de etabs)
	smodel.SetModelIsLocked(False)
	# 'initialize model | Inicializa nuevo modelo en blanco
	resUnit = smodel.InitializeNewModel()

	namef = "example03.edb"
	# if savef.saveFile(smodel, namef):
	# 	print('success')

	# estado, namef = openf.openFile(smodel, namef)
	# print(estado)

	# 
