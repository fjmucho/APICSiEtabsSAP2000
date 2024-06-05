import sys
# import comtypes
from comtypes.client import CreateObject

try:
    # Connecting | coneccion
    xl = CreateObject("Excel.Application")
except (OSError, comtypes.COMError):
    print("No tiene instalada el programa(Excel).")
    sys.exit(-1)
    
xl.Workbooks.Add()
# help(engine)

from comtypes.gen.Excel import xlRangeValueDefault

xl.Range["A1", "C1"].Value[xlRangeValueDefault] = (10,"20",31.4)


# print (xl.Range["A1", "C1"].Value[xlRangeValueDefault](10, "20", 31.4))
print (xl.Range["A1", "C1"].Value[xlRangeValueDefault])

print (xl.Range["A1", "C1"].Value())

xl.Range["A1", "C1"].Value[:] = (3, 2, 1)
xl.Range["A1", "C1"].Value[()] = (1, 2, 3)

print (xl.Range["A1", "C1"].Value[:])
print (xl.Range["A1", "C1"].Value[()])