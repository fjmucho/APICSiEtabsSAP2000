# Breve Introducción a la API de CSI y Autodesk

## Sap2000API
Easy to use functions written in Cshar/Python/VisualBasic/Matlab for the CSI Sap2000 API

## EtabsAPI
Easy to use functions written in Cshar/Python/VisualBasic/Matlab for the CSI Etabs API


### Objective

To development functionalities to increase the usability of CSI Etabs and provide some custom functions(synchronised) Python to CSI Etabs for data extraction and send, on Structural Design using 

Peruvian Standards.

This project is intended to help those who are looking to develop there own programs to
supplement their design workflows. People are encouraged to help contribute with their own
functions or send suggestions for tools that Engineers may find useful. 


## Estructura del Proyecto

El proyecto está organizado en las siguientes carpetas:

```plaintext
📁 APICSiEtabsSAP2000
│
├── 📁 docs         # docuementation of the code writed in this repository for C#, Python, ...
├── 📁 srcCshar     # Source code using C# for API
├── 📁 srcOctave    # Source code using Octave for API
├── 📁 srcPython    # Source code using Python for API
└── README.md       # Este archivo
```

### Current Capabilities

- Connect to the Excel(Microsoft Office) API using python
- Connect to the Etabs API using python, C#, C++, ...

### Dependencies Cshar and Visual Basic

* [.Net](https://dotnet.microsoft.com/) version 5.0.201+

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

## References
<!-- - https://hakan-keskin.medium.com/ -->


