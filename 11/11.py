matrix = [[int(x) for x in line.strip()] for line in open('11.input')]
xs, ys = len(matrix), len(matrix[0])

def flash(x,y,m):
	for x1 in range(x-1,x+2):
		for y1 in range(y-1, y+2):
			if x1 != x or y1 != y:
				add(x1, y1, m)

def add(x,y,m):
	if 0 <= x < xs and 0 <= y < ys:
		m[x][y] += 1
		if m[x][y] == 10:
			flash(x,y,m)

a = 0
b = None

for s in range(10000):
	for x in range(xs):
		for y in range(ys):
			add(x,y,matrix)

	matrix = [[v if v < 10 else 0 for v in x] for x in matrix]
	flashes = sum([1 for x in matrix for v in x if v == 0])

	if s < 100:
		a += flashes

	if not b and flashes == xs * ys:
		b = s + 1

	if b and s > 99:
		break

print(f"a: {a}")
print(f"b: {b}")

matrix = [[int(x) for x in line.strip()] for line in open('11.input')]

a2 = 0
h,w = len(matrix), len(matrix[0])
for s in range(1,1000):
	wl = [(x,y) for x in range(h) for y in range(w)]

	while wl:
		x,y = wl.pop(0)
		if 0 <= x < h and 0 <= y < w:
			matrix[x][y] += 1
			if matrix[x][y] == 10:
				wl += [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]

	matrix = [[v if v < 10 else 0 for v in x] for x in matrix]
	fl = sum([1 for x in matrix for v in x if v == 0])

	if s < 101:
		a2 += fl

	if fl == h * w:
		print(f"a2: {a2}\nb2: {s}")
		break
