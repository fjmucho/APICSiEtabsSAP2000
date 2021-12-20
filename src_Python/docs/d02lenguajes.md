# Fundamentos de programacion [`C#`, `VB`, `C++`, `F#`, `Python`, `Matlab`]


### Data types
    
#### Numeric types

#### Booleans

#### Strings

#### Arrays

### Operators


#### Arithmetic operators
```cs
// C Sharb (C#)
vnuma = 10
vnumb = 20
vresult = vnuma + vnumb // Addition
vresult = vnuma - vnumb // Subtraction
vresult = vnuma * vnumb // Multiplication
vresult = vnuma / vnumb // Division
```

```vb
' Visual Basic
vnuma = 10
vnumb = 20
vresult = vnuma + vnumb ' Addition
vresult = vnuma - vnumb ' Subtraction
vresult = vnuma * vnumb ' Multiplication
vresult = vnuma / vnumb ' Division
```

```matlab
% matlab, aqui las bariables son arreglos por definicion.
vnuma, vnumb = 10, 20
vresult = vnuma + vnumb % Addition
vresult = vnuma - vnumb % Subtraction
vresult = vnuma * vnumb % Multiplication
vresult = vnuma / vnumb % Division
```

```python
# Python
vresult = None
vnuma , vnumb = 10, 20
vresult = vnuma + vnumb # Addition
vresult = vnuma - vnumb # Subtraction
vresult = vnuma * vnumb # Multiplication
vresult = vnuma / vnumb # Division
```

#### Relational operators
```cs
// Code cshar 

```

```vb
' code visual basic 

```

```matlab
% matlab
vresult = vnuma == vnumb  % Equal
vresult = vnuma > vnumb   % Greater than
vresult = vnuma < vnumb   % Less than
vresult = vnuma >= vnumb  % Greater than or equal
vresult = vnuma <= vnumb  % Less than or equal
vresult = vnuma ~= vnumb  % Not equal
```

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
```cs
// Code cshar 
```

```vb
' code visual basic 
```

```matlab
% matlab
vnuma && vnumb      % Short-circuit logical AND
vnuma || vnumb      % Short-circuit logical OR
vnuma & vnumb       % Element-wise logical AND
vnuma | vnumb       % Element-wise logical OR
xor(vnuma, vnumb)   % Logical EXCLUSIVE OR
~vnuma              % Logical NOT
```

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

```vb
' code visual basic 
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

```vb
' code visual basic 
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
```

```vb
' code visual basic 
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
```

```vb
' code visual basic 
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
```

```vb
' code visual basic 
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
```

```vb
' code visual basic 
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
```

```vb
' code visual basic 
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

General syntax:
```cs
// Code cshar 
```

```vb
' code visual basic 
```

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

Calling functions:
```cs
// Code cshar 
```

```vb
' code visual basic 
```

```matlab
% Calling MyFun, on matlab
[out1, out2, ...] = MyFun(arg1, arg2, ...)
```

```python
# Calling MyFun, on python
out1, out2, ... = MyFun(arg1, arg2, ...)
```

A simple example:
```cs
// Code cshar 
```

```vb
' code visual basic 
```

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

General syntax:
```cs
// Code cshar 
```

```vb
' code visual basic 
```

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