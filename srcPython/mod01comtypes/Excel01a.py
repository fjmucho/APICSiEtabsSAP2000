#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Para usar esta script tiene que estar ejecutandose Excel.
1. Nos conectamos
"""

import comtypes.client

try:
	# Connecting | coneccion
	EXCELObject = comtypes.client.GetActiveObject("Excel.Application") 
except (OSError, comtypes.COMError):
	print("No tiene instalada el programa(Excel).")
	sys.exit(-1)
# xl.Visible = True
# wb = xl.Workbooks.Add()
# sheet = wb.ActiveSheet
# sheet.Range["A1"].Value2 = "Test passed"
# wb.Close(SaveChanges = False)
# xl.Quit()
# Mostramos los metodos y propiedades con las que contamos
print(dir(EXCELObject))
exit()


'''
['ActivateMicrosoftApp', 
'ActiveCell', 
'ActiveChart', 
'ActiveDialog', 
'ActiveEncryptionSession', 
'ActiveMenuBar', 
'ActivePrinter', 
'GetActiveObject'
...
'_needs_com_addref_', 
'_objects', 
'_type_', 
'from_param', 
'value']
'''