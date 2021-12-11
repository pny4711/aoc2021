from functools import reduce

a = reduce(lambda s, e : (s[0] + 1, int(e)) if s[1] and int(e) > s[1] else (s[0], int(e)), open('1.input'), (0,None))
print(f"A: {a[0]}")

x = [int(line.strip()) for line in open("1.input")]
y = [(v + x[i+1] + x[i+2]) for i, v in enumerate(x[:-2])]
a = sum([(v > x[j]) for j, v in enumerate(x[1:])])
b = sum([(v > y[j]) for j, v in enumerate(y[1:])])

print(f"A: {a}")
print(f"B: {b}")