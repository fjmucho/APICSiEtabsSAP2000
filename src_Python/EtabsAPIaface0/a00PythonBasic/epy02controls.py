# evalua una nota aprobatoria 1 de 10.
nota = 7
if 9.5 <= nota < 11: print("Excelente")
elif 8.5 <= nota < 9.5: print("Muy bien")
elif 7.5 <= nota < 8.5: print("Bien")
elif 7.0 <= nota < 7.5: print("Regular")
else: print("No aprobado")

num = [2,1,3,5,2]
for _ in num:
	print(_, end=',')
print()

'''
secuencia se denomina de Ulam. 
x =	|x/2,  x es par
	|3x+1, x es impar
'''
x=11
while x>1:
    if x%2 == 0: x=x//2
    else: x=3*x+1
    print(x,end="-")
