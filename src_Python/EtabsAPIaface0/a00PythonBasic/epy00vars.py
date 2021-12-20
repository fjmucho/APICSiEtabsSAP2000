# 1. Console
# ...
# 2. Data Estructures
vnumi = 1

vnumf = 1.001

vstr = "Hello"

vbool = True

vlist = [
	1,-34,
	"Word1",'Word2',
	(1,2),[1,2,3],
	{'one':2,'two':3,'three':5}
	]
vlist[0]=30

vtuple = (1,
	-34,
	"Word1",
	'Word2',
	(1,2),
	[1,2,3],
	{'one':2,'two':3,'three':5}
	)
# vtuple[0]=30 # Esto lanzara un eror poque es inmutable
vdict = {"Word":"Hello","word2":"Bye"}

print(type(vnumi), id(vnumi), hex(id(vnumi)), vnumi)
print(type(vnumf), id(vnumf), hex(id(vnumf)), vnumf)
print(type(vstr), id(vstr), hex(id(vstr)), vstr)
print(type(vbool), id(vbool), hex(id(vbool)), vbool)
print(type(vlist), id(vlist), hex(id(vlist)), vlist)
print(type(vtuple), id(vtuple), hex(id(vtuple)), vtuple)
print(type(vdict), id(vdict), hex(id(vdict)), vdict)