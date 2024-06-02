import sys
import comtypes
from comtypes.client import CreateObject

try:
	# Connecting | coneccion
	xl = CreateObject("Excel.Application")
except (OSError, comtypes.COMError):
	print("No tiene instalada el programa(Excel).")
	sys.exit(-1)


xl.Visible = True
print (xl)