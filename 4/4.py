boards = []

lines = [l.strip() for l in open('4.input.txt')]
numbers = [int(n) for n in lines[0].split(',')]

for x in range((len(lines)-1) // 6):
	boards.append([[int(v) for v in lines[x*6+y+1].split()] for y in range(1,6)])

vinners = []

for n in numbers:
	changed = []

	for b in boards:
		for bl in b:
			for i in range(5):
				if bl[i] == n:
					bl[i] = 0
					if b not in changed:
						changed.append(b)

	for b in changed:
		if (not (all([sum(bl) for bl in b]) and
			     all([sum([ b[l][c] for l in range(5)]) for c in range(5)]))):
			vinners.append(n * sum([sum(bl) for bl in b]))
			boards.remove(b)

print(f"A: {vinners[0]}")
print(f"B: {vinners[-1]}")
