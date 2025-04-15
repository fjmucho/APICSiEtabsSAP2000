# Requerimientos 
* dotnet languaje C#
* vscode 

## intructions | instrucciones

### Dependencies Cshar and Visual Basic

* [.Net](https://dotnet.microsoft.com/) version 5.0.201+

### console apps projects

```bash
> mkdir Projects
> cd Projects
> dotnet new console -o myApp
> cd myApp
# en caso que sea un solo proyecto 
> dotnet run
# si tiene muchos scripts/archivos y se quiere ejecutar por script
> dotnet run Program.cs
```

## create new project | crear nuevo proyecto
````cmd
> dotnet new console -o CSiAPI_Intro

Esto es .NET 5.0.s
---------------------
Versión del SDK: 5.0.201

Telemetría
---------
Las herramientas de .NET recopilan datos de uso para ayudarnos a mejorar su experiencia. Microsoft los recopila y los comparte con la comunidad. Puede optar por no participar en la telemetría si establece la variable de entorno DOTNET_CLI_TELEMETRY_OPTOUT en "1" o "true" mediante su shell favorito.

Lea más sobre la telemetría de las herramientas de la CLI de .NET: https://aka.ms/dotnet-cli-telemetry

----------------
Se instaló un certificado de desarrollo con HTTPS para ASP.NET Core.
Para confiar en el certificado, ejecute "dotnet dev-certs https --trust" (solo Windows y macOS).
Obtenga más información sobre HTTPS: https://aka.ms/dotnet-https
----------------
Escriba su primera aplicación: https://aka.ms/dotnet-hello-world
Descubra las novedades: https://aka.ms/dotnet-whats-new
Explore la documentación: https://aka.ms/dotnet-docs
Notifique los problemas y busque el código fuente en GitHub: https://github.com/dotnet/core
Use "dotnet --help" para ver los comandos disponibles o visite: https://aka.ms/dotnet-cli
--------------------------------------------------------------------------------------
Getting ready...
The template "Console Application" was created successfully.

Processing post-creation actions...
Running 'dotnet restore' on CSiAPI_Intro\CSiAPI_Intro.csproj...
  Determinando los proyectos que se van a restaurar...
  Se ha restaurado C:\Users\Francisco\Documents\PyEtabsAPI\src_Cshar\CSiAPI_Intro\CSiAPI_Intro.csproj (en 202 ms).
Restore succeeded.

> cd myApp
> dotnet run
Hello World!
````