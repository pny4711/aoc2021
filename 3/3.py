dig = None

data = [[int(d) for d in line.strip()] for line in open('3.input')]
w = len(data[0])

def mc(l, b): return 1 if sum([n[b] for n in l]) * 2 >= len(l) else 0
def lc(l, b): return 1 - mc(l, b)
def val(num):
	return sum([ v << (len(num) - 1 - i) for i,v in enumerate(num)])

e = val([mc(data, i) for i in range(w)])
g = val([lc(data, i) for i in range(w)])

print(f"a: {e*g} {e} * {g}")

odata = [num for num in data]
cdata = [num for num in data]

for i in range(w):
	m = mc(odata, i)
	l = lc(cdata, i)
	if len(odata) > 1:
		odata = [num for num in odata if num[i] == m]
	if len(cdata) > 1:
		cdata = [num for num in cdata if num[i] == l]

o = val(odata[0])
c = val(cdata[0])

print(f"b: {o*c} {o} * {c}")

