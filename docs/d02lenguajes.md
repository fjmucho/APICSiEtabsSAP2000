# Fundamentos de programacion [`C#`, `VB`, `C++`, `F#`, `Python`, `Matlab`]


### Fundamentos

- Numeric types
- Booleans
- Strings
- Operators
- Arithmetic operators
- Relational operators
- Logical operators
- Variables
- Arrays
- Control Flow
- functions
- Object-Oriented programing

Lenguaje visual basic (.vb)
```vb
' Comentarios, Salidas y entradas estandar con VB
Imports System.IO 'Esta libreria es para archivos -- StreamWriter, Streamreader

Module Module1

    Sub Main()

        ' 
        'Declaracion de variables
        ' 
        Dim varObject               ' Guarda la variable como un objeto(Consumo de memoria es más) 

        Dim op1, op2 As String      'Cadenas alfanumericos
        'Dim op3 As String
        Dim result As String

        Dim msg As String

        Dim crt As Char             ' 0 - 65535

        Dim AndOrXor As Boolean     ' true or false

        Dim edad As Byte            ' 0 - 255
        edad = 25
        Dim contador As Integer     ' 
        Dim cont As Long            ' 

        ' vars for matrix
        Dim colores(2) As String ' se vuelve en un array de tres valores
        ' Matrix multidimencional
        Dim agenda(3, 100) As String

        Dim fecha As Date
        'fecha = "01/06/2016 12:16:00" ' dia/mes/año
        fecha = #01/06/2016 12:16:00# ' mes/dia/año 
        Console.WriteLine(fecha)

        ' comentario de una sola linia - coment line only
        Console.WriteLine("Welcme to VB")
        Console.Write("Esto es valido")
        Console.WriteLine(" tambien")

        ' operadores matematicos
        ' +         suma
        ' -         resta
        ' *         multiplicacion
        ' /         division
        ' \         division
        ' Mod       resto
        ' ^         potencia
        ' & ó +     concatenar cadenas
        Console.WriteLine(AndOrXor)
        op1 = "Operador de tipo"
        op2 = " String"
        result = op1 & op2 ' +(para concatenar)
        ' Console.WriteLine("\nEl resultado es: ", result)
        Console.Write("El resultado es: ")
        Console.WriteLine(result)

        ' Abreviados, mas optimizado
        ' +=         suma
        ' -=         resta
        ' *=         multiplicacion
        ' /=         divicion
        '  =         division
        ' ^=         potencia
        ' &= ó +=     concatenar cadenas
        op1 &= op2
        Console.Write("El resultado es: ")
        Console.WriteLine(op1)

        ' operadores lógicos
        ' >         Mayor que
        ' <         Menor que
        ' >=        Mayor o igual que
        ' <=        Menor o igual que 
        ' ==        Igual que
        ' !=        Es diferente
        ' <>        Es mayor que o es menor que
        ' like      Es parecido
        ' And       y
        ' Or        o
        ' Xor       o exclusivo (and o or) 
        Console.Write("El resultado es: ")
        Console.WriteLine(AndOrXor) ' false
        AndOrXor = 10 = 10
        Console.WriteLine(AndOrXor) ' true
        AndOrXor = ("H" = "m") Xor (5 < 10) ' false Xor false = true
        Console.Write("El resultado ahora es: ")
        Console.WriteLine(AndOrXor) ' true

        ' Comparadores
        Console.WriteLine()
        op1 = "M" ' 77
        op2 = "m" ' 109
        'Asc("m") ' transforma de cadena a binario
        result = Chr(109) ' Transforma de binario a cadena
        Console.Write("El resultado es: ")
        Console.WriteLine(result)

        ' Patrones
        Console.WriteLine()
        msg = "m" Like "[!A-Z]" ' evalua en formato binario
        Console.Write("El resultado es: ")
        Console.WriteLine(msg)

        ' Comparacion con patrones
        result = "2016" Like "##16" ' para tipos numericos
        ' result = "H2la" Like "H?la" 'remplazar en lugar de ? un caracter diferente
        ' result = "Esto es un texto" Like "Esto es un *" ' Es parecido al texto
        Console.WriteLine(result)

        '
        ' -- Condicionales --
        '

        'if else
        Console.WriteLine()
        Console.WriteLine("--> If-Else")
        If edad <> 20 Then Console.WriteLine("En esta sentencias no es necesario un: End If")
        If edad < 20 Then
            If edad < 10 Then
                msg = "Tienes menos de diez años"
            Else
                msg = "Tienes entre 10 y 20 años"
            End If
        Else
            If edad < 30 Then
                msg = "Eres un veinteañero"
            Else
                msg = "Tienes muchos años"
            End If
        End If
        Console.WriteLine("No se que edad tienes")

        ' Select case
        Console.WriteLine()
        Console.WriteLine("--> Select Case n")
        Select Case edad
            Case Is < 0 ' caso es operador_Logico valor
                msg = "Aun No as nacido"
            Case 0
                msg = "¡Acabas de nacer!"
            Case 1 To 10
                msg = "Tienes de 1 a 10 años"
            Case 10 To 20
                msg = "Tienes de 10 a 20 años"
            Case 20 To 30
                msg = "Tienes de 20 a 30 años"
            Case 40, 50, 60 ' Casos multiples
                msg = "Eres mayor de edad"
            Case Else ' En otro caso
                msg = "No se que edad tienes"
        End Select
        Console.WriteLine(msg)

        '
        ' -- Loops --
        '

        ' While
        Console.WriteLine("")
        contador = 0
        While contador < 4
            Console.Write("While: ")
            Console.WriteLine(contador)
            contador += 1
        End While
        Console.WriteLine("Ya he salido del bucle While")

        ' Do - Loop While
        Console.WriteLine("")
        contador = 0
        Do
            Console.Write("Do Loop While: ")
            Console.WriteLine(contador)
            contador += 1
            ' If contador > 100 Then Exit Do
            ' Loop
        Loop While contador < 4 ' Do Until contador > -5
        Console.WriteLine("Ya he salido del bucle Do Loop While")

        Do Until contador < 0 ' Do While contador < 4
            Console.Write("Do Until: ")
            Console.WriteLine(contador)
            contador -= 1
        Loop

        ' For
        Console.WriteLine("")
        ' For contador = 0 To 6 ' se incrementa por defecto en 1
        For contador = 0 To 6 Step 1
            Console.Write(" For: ")
            Console.WriteLine(contador)
            ' Exit For ' es igual que break en otros lenguajes
            If contador = 4 Then Exit For
        Next
        Console.WriteLine("Ya he salido del bucle For")

        '
        ' -- Arrays --
        '

        ' Matris unidimencional
        Console.WriteLine("")
        Console.WriteLine("Matrices:")
        colores(0) = "Rojo"
        colores(1) = "Verde"
        colores(2) = "Azul"
        ' ReDim colores(5) ' Redimencionando el array, Incrementar en 3 espacios mas pero borra todo su contenido del array
        ReDim Preserve colores(5) ' Redimencionando el array, Incrementar en 3 espacios mas
        colores(3) = "Magenta"
        colores(4) = "Cian"
        colores(5) = "Amarillo"
        Console.Write("Los colores almacenados son: ")
        ' Console.Write("Color: "& color(0))
        Dim tm As Integer
        tm = UBound(colores)
        For contador = 0 To tm
            Console.Write(colores(contador) & ", ")
        Next

        ' Matrices Multidimencionales
        Console.WriteLine()
        agenda(0, 0) = "Jose Vicente"
        agenda(1, 0) = "5312452345"
        agenda(2, 0) = "Direccion de la calle"
        agenda(3, 0) = "info@jocarsa.com"
        'otro dato
        agenda(0, 1) = "Javier"
        agenda(1, 1) = "53455"
        agenda(2, 1) = "Calle 2, 43"
        agenda(3, 1) = "fqsdrf@tfsdsdf.com"
        'otro mas
        agenda(0, 2) = "Juan"
        agenda(1, 2) = "75676574"
        agenda(2, 2) = "Calle 3, 65"
        agenda(3, 2) = "gsdfgsd@fdsafsd.com"
        Console.WriteLine()
        Console.WriteLine("Nombre: " & agenda(0, 1))
        Console.WriteLine("Telefono: " & agenda(1, 1))
        Console.WriteLine("TDireccion: " & agenda(2, 1))
        Console.WriteLine("Email: " & agenda(3, 1))


        ' 
        '  Files -- Write, read. info
        ' 
        Dim escribir As StreamWriter
        Dim leer As StreamReader
        Dim linia As String
        Dim archivo As String
        Dim informacion As FileInfo

        ' StreamWriter - escritura y sobrescritura
        Console.WriteLine()
        'escritor = New StreamWriter("C:/archivos/prueba.txt", False)
        ' false lo q hace es borrar y sobrescribir, pero en caso de true lo q hace es escribir despues del contenido
        escribir = New StreamWriter("./ArchivoIO.txt", False)
        escribir.Write("Hola me llamo Francisco JM")
        escribir.Close()

        ' StreamReader
        Console.WriteLine()
        leer = New StreamReader("./ArchivoIO.txt")
        linia = leer.ReadToEnd() ' Leer hasta el final del archivo
        Console.WriteLine("Contenido: ")
        Console.WriteLine(linia)

        ' FileInfo
        Console.WriteLine()
        'archivo = "C:/archivos/prueba.txt"
        archivo = "./ArchivoIO.txt"
        informacion = New FileInfo(archivo)
        Console.WriteLine("El nombre del archivo es: " & informacion.Name)
        Console.WriteLine("La extension del archivo es: " & informacion.Extension)
        Console.WriteLine("La ultima vez que accedi al archivo fue: " & informacion.LastWriteTime)

        ' 
        ' Objetos
        ' 
        Console.WriteLine()
        'guau es una instancia a un objeto, puede ser otra palabra
        Dim guau As Object
        guau = New digoHola()
        guau.hola() ' llamando al metodo hola
        guau.adios() ' Llmando al metodo adios

        Console.ReadLine()

    End Sub

End Module

' Objetos
Public Class digoHola
    Dim texto As String
    Public Sub hola()
        Console.WriteLine("Clase digoHola y acceso al Metodo hola")
    End Sub
    Public Sub adios()
        Console.WriteLine("Clase digoHola y acceso al Metodo adios")
    End Sub
End Class
```

#### Arithmetic operators | Operadores aritméticos

En Lenguaje C# (.cs)
```cs
// CShar (C#)
using System;

namespace HolaMundo
{
    class Program
    {   
        static void Main()
        {
            Console.Title = "Operadores";
            int a=5, b=5;
            var opA = a + b;
            var opS = a - b;
            var opSo = -opS;
            var opM = a * b;
            var opD = a / b;
            var opM = a % b;

            a++;
            b--;
            --opA;
            opA += opS; // opA = opA+opS
            Console.WriteLine(opA);

            Console.ReadKey();
        }
    }
}
```
En lenguaje Octave o Matlab y Scilab
```matlab
% matlab, aqui las bariables son arreglos por definicion.
vnuma, vnumb = 10, 20
vresult = vnuma + vnumb % Addition
vresult = vnuma - vnumb % Subtraction
vresult = vnuma * vnumb % Multiplication
vresult = vnuma / vnumb % Division
```
EN lenguaje Python (.py) y Ruby (con peque;a modificacion)
```python
# Python
vresult = None
vnuma , vnumb = 10, 20
vresult = vnuma + vnumb # Addition
vresult = vnuma - vnumb # Subtraction
vresult = vnuma * vnumb # Multiplication
vresult = vnuma / vnumb # Division
```

#### Relational operators | Operadores relacionales

En lenguaje C#
```cs
// Code cshar 

```
En lenguaje Octave
```matlab
% matlab
vresult = vnuma == vnumb  % Equal
vresult = vnuma > vnumb   % Greater than
vresult = vnuma < vnumb   % Less than
vresult = vnuma >= vnumb  % Greater than or equal
vresult = vnuma <= vnumb  % Less than or equal
vresult = vnuma ~= vnumb  % Not equal
```
En lenguaje Python
```python
# python
vresult = vnuma == vnumb  # Equal
vresult = vnuma > vnumb   # Greater than
vresult = vnuma < vnumb   # Less than
vresult = vnuma >= vnumb  # Greater than or equal
vresult = vnuma <= vnumb  # Less than or equal
vresult = vnuma != vnumb  # Not equal
```

#### Logical operators

En lenguaje C#
```cs
// Code cshar 

```
En lenguaje Octave
```matlab
% matlab
vnuma && vnumb      % Short-circuit logical AND
vnuma || vnumb      % Short-circuit logical OR
vnuma & vnumb       % Element-wise logical AND
vnuma | vnumb       % Element-wise logical OR
xor(vnuma, vnumb)   % Logical EXCLUSIVE OR
~vnuma              % Logical NOT
```
En lenguaje Python
```python
# python
vnuma and vnumb     # Short-circuit logical AND
vnuma or vnumb      # Short-circuit logical OR
vnuma and vnumb     # Element-wise logical AND
vnuma or vnumb      # Element-wise logical OR
vnuma ^ vnumb       # Logical EXCLUSIVE OR
not vnuma       # Logical NOT
```


### Variables

Assign variables:

```cs
// Code cshar 
```

```matlab
% Assign variables
vnuma = 10;
```

```python
# Assign variables
vnuma = 10
```

Multi assign:
```cs
// Code cshar 
```

```matlab
% matlab tiene soporte
% Unsupported
```

```python
# Multi assign
# vnuma = 10 
# vnumb = 20
# vnumc = 30
vnuma, vnumb, vnumc = 10, 20, 30
```

### Control flow

#### if-else if-else

Only `if`:
```cs
// Code cshar 
using System;

namespace UsandoCshar
{
    class Condicionales
    {
        static void Main(string[] args)
        {
            Console.Title("Conditionals...");
            string msg = "";
            sbyte bt = 127;
            int f = 10;

        //if(basic) Statement
            Console.WriteLine("if -> basico.");
            if (bt > 023) //023 = 19
                msg = "verda";

            //Uso necesario de las llaves
            if (bt > 012)//012 = 10
            {
                msg = "es";
                msg += " verda";
            }

            //if(multiple)
            Console.WriteLine("if -> anidadnos: ");
            if (f > 0)
            {
                if (f < 15)
                {
                    if (f != 0)
                        if (f == 5)
                            msg = "es igual a "+f;
                    msg = "...es diferente, y esta entre __ hasta __";// esto sirve de else.
                }
                if (f == 10)
                    msg = "Es igual a " + f;
            }

            //Console.ReadKey();
        }
    }
}
```

```matlab
% matlab
% Using if
text = "C:\Program Files\Computers and Structures\ETABS 19\ETABS.exe"
xts = [-4:] % revisar y hacer pruebas
if xts == ".exe"
    disp('Su extension es: ', xts);
end
disp("no es una aplicacion ejecutable para windows");
```

```python
# python
text = "C:\Program Files\Computers and Structures\ETABS 19\ETABS.exe"
xts = text[-4:]#xts: extension (.exe, .edb, etc)
if xts==".exe":
    print(f"Su extension es: {xts}")
print("no es una aplicacion ejecutable para windows")
```

`if-else` structure:
```cs
// Code cshar 
using System;

namespace UsandoCshar
{
    class Condicionales
    {
        static void Main(string[] args)
        {
            Console.Title("Conditionals...");
            string msg = "";
            sbyte bt = 127;

            //Statement - if else
            Console.WriteLine("if else -> basico");
            if (msg.Equals("Francisco")) {
                msg = "La cadena es igual";
            } else
                msg = "No es igual la cadena";

            //if else anidados
            Console.WriteLine("if else-if else -> anidado");
            if (bt < -128)
                msg = "Not type byte - No es de tipo byte " + bt;
            else if (bt > 127)
                msg = "not type byte - No es de tipo byte " + bt;
            else
                msg = "If(){}else{} -> basic: is type byte " + bt;

            //Console.ReadKey();
        }
    }
}
```

```matlab
% matlab
n = 1
if n > 0
    disp('n is positive');
else
    disp('n is negative or zero');
end
```

```python
# python
n = 1
if n > 0:
    print('n is positive')
else:
    print('n is negative or zero')
```

#### For loop
```cs
// Code cshar 
using System;
using System.Collections.Generic;

class MainClass
{
	class Promgram
	{
		public static void Main()
		{
            Console.Title("Loops");
	
            string msg = "abcdefgh...z"


            List<char> listaLetras = new List<char>();
            for(int i=0; i <= msg.Length-1; i++)
            {
                //char letra = msg[i];
                //Console.WriteLine(letra);
                listaLetras.Add(msg[i]);
            } 
            foreach(char letra in listaLetras)
            {
                Console.WriteLine(letra);
            }
            /*
             Hacer un programa que encuentre los
             números primos que existen entre el 1 y el 1000.
             */
            //Break and Continue
            for (var i = 0; i < 5; i++)
            {
                if (i == 2)
                {
                    continue;
                }
                else if (i == 4)
                {
                    break;
                }
                Console.WriteLine("Break and Continue " + i);
            }
		}
	}
}
```

```matlab
% for loop matlab
for i = 1:10
    disp(i)
end
```

```python
# for loop python
for i in range(1,11):
    print(i)
```

#### While loop
```cs
// Code cshar 
using System;
using System.Collections.Generic;

class MainClass
{
	class Promgram
	{
		public static void Main()
		{
            Console.Title("Loops");

            var dwl = 5;
            do
            {
                Console.WriteLine("do-while -> " + dwl--);
                //Console.WriteLine("para terminar ingrese S.");
                //respuesta = Console.ReadLine();
            } while (dwl > 0);
            //} while (dwl == 'S');

            var wl = 0;
            while (wl < 5)
            {
                Console.WriteLine("while -> " + wl++);
                //console.debug(" "+wl);
                //document.write(wl," ");
            }
            
		}
	}

}
```

```matlab
% while loop matlab
a = 1
while a < 10
    disp(a);
    a = a + 1;
end
```

```python
# while loop python
a = 1
while a < 10:
    print(a)
     a += 1
```

#### Try - Catch
```cs
// Code cshar 
using System;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EnumsYEstructs {

	class Program 
	{
		static void hacerTrabajo() 
		{
			Fecha fecha_x_Defecto = new Fecha();
			Console.WriteLine(fecha_x_Defecto);
			Fecha.fechaRecordar = new Fecha(2014, Mes.Septiembre, 11);
			Console.WriteLine(fechaRecordar);
		}

		static void Main(string[] args) 
		{
			try
			{
				Console.WriteLine(ex.Message);			
			}
			catch (System.Exception)
			{
				hacerTrabajo(Exception ex);
				//throw;
			}
			
		}
	}
}
```

```matlab
% on matlab
try
    % Do something ...
catch err
    % On failure
end
```

```python
# on python
try:
    # Do something
except Exception:
    # On failure
end
```

### Functions

#### Creating a function

Sintaxis:

```matlab
function [out1, out2,...] = MyFun(arg1, arg2, ...)
% Code here...
% out1 = some1
% out2 = some2
% ...
end
```

```python
def MyFun(arg1, arg2, ...):
    # Code python here ...
    return out1, out2, ...
```

```matlab
% Calling MyFun, on matlab
[out1, out2, ...] = MyFun(arg1, arg2, ...)
```

```python
# Calling MyFun, on python
out1, out2, ... = MyFun(arg1, arg2, ...)
```

**A simple example:**

En lengauje C#
```cs
// Code cshar 
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

class MainClass
{
	class Promgram
	{
		public static void Main()
		{

            // func que ejecutan codigo.

            // func que regresan un valor

            // func que reciben parametros

            // func que reciben parametros y regresan valor

            // paso por copia y referencia.
            var anum = 5; int bnum = 3;
            Console.WriteLine("Antes -> {0}, {1}", anum, bnum);
            fun_x_copy(anum);//paso por copia

            fun_x_ref(ref anum, ref bnum);//paso por referencia
            Console.WriteLine("Despues -> {0}, {1}", anum, bnum);

            // uso de parametros default.
            int k = 0;
            k = fun_p_def(anum, 3);//anum=3
            Console.WriteLine("Parametros por defecto -> {0}, {1}", k, fun_p_def(anum));
		}

	//Funcion por copia
        static void fun_x_copy(int p)
        {
            p = 14;
        }
    //Funcion por referencia
        static void fun_x_ref(ref int xnum, ref int ynum)
        {
            int temp = 0;

            temp = xnum;
            xnum = ynum;
            ynum = temp;
        }
    //Funcion con paso de parametros por defecto
        static int fun_p_def(int pd, int p_def=2)
        {
            return pd*p_def;
        }
	}
}

```
En lenguaje Octave o Matlab
```matlab
% on matlab
function r = iseven(n)
if ((-1)^n) == 1
    r = True;
else
    r = False;
end
end
```
En lenguaje python
```python
# on python
def iseven(n):
    if ((-1)**n)==1:
        return True
    return False
```

## Object-Oriented Programming

- Defining class

### Defining class

En lenguje C#
```cs
// Code cshar, no es necesario un ejemplo
```

En lenguaje Octave o Matlab
```matlab
classdef MyClass
% Help of class
% 
    properties
        % class properties
    end

    methods
        function obj = MyClass(args)
            % Constructor
        end

        % other methods
        function OneMethod(obj,one_args)
            % Method ...
        end

        function OtherMethod(obj,other_args)
            % Method ...
        end
    end
end
```

En lenguaje python
```python
class MyClass():
    def __init__(self,args):
        # Constructor
        # Class properties are defined here

    def OneMethod(self,one_args):
        # Method

    def OtherMethod(self,other_args):
        # Method
```