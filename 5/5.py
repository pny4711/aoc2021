lines = [[[int(v) for v in p.split(',')] for p in l.strip().split('->')]
         for l in open('5.input.txt')]

m = 1 + max([max(l[0] + l[1]) for l in lines])
wa = [[0 for x in range(m)] for y in range(m)]

for (x1, y1), (x2, y2) in lines:
    if x1 != x2 and y1 != y2:
        continue
    for y in range(min(y1,y2), max(y1,y2) +1):
        for x in range(min(x1,x2), max(x1,x2) +1):
            wa[y][x] += 1

a = sum([sum([1 for x in range(m) if wa[y][x] > 1]) for y in range(m)])

for (x1, y1), (x2, y2) in lines:
    if x1 != x2 and y1 != y2:
        x, y = x1, y1
        while x != x2 and y != y2:
            wa[y][x] += 1
            x += 1 if x2 > x1 else -1 if x2 < x1 else 0
            y += 1 if y2 > y1 else -1 if y2 < y1 else 0
        wa[y][x] += 1

b = sum([sum([1 for x in range(m) if wa[y][x] > 1]) for y in range(m)])

print(f"a: {a}")
print(f"a: {b}")
