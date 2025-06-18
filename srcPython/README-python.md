

## intructions | instrucciones

### Dependencies python

The following packages are required:

* [comtypes](https://pypi.org/project/comtypes/) version 1.1.9+
* [pandas](https://pandas.pydata.org/) version 1.2.3+
* [PyQt6](https://wiki.qt.io/Qt_6.0_Release) version 6.0.3+
* NumPy
* Matplotlib
* EZDXF

Puedes instalar las dependencias ejecutando el siguiente comando para el caso de python:

```bash
pip install -r requirements.txt
```
acerca de como usar en cada lenguaje esta en el directorio `docs` mas informacion.

### Uso del Proyecto - Clonar el repositorio

Primero, clona el repositorio en tu máquina local:

```bash
git clone https://github.com/fjmucho/APICSiEtabsSAP2000.git
cd APICSiEtabsSAP2000
```

## Errores comues
ir a la ruta y ejecutar como administrador los siguentes ejecutables: UnRegisterETABS.exe y RegisterETABS.exe y en caso de SAP200 serian: UnregisterSAP2000.exe y RegisterSAP2000.exe.
```cmd
> C:\Program Files\Computers and Structures\SAP2000 26\UnRegisterETABS.exe

> C:\Program Files\Computers and Structures\ETABS 20\UnregisterSAP2000.exe
```
seguidamente se debe probar la coneccion a la aplicacion.

## References
- 1. github [sap2000](https://github.com/kandluis/sap2000)
- 2. github [etabs_api](https://github.com/ebrahimraeyat/etabs_api)
- 3. github [pytabs](https://github.com/mitchell-tesch/pytabs)
- 4. Librería para el Análisis Sísmico según NTE [E.030](https://pypi.org/project/E030/) de Perú
- a. https://hakan-keskin.medium.com/
- b. https://www.youtube.com/playlist?list=PLtZFoNK7ZKaUgc2i3g98xXLsl-uWw0mgn
- c. https://www.facebook.com/StructuralTech.py/videos/1890176388442498/