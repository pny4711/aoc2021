from functools import reduce

def f(p, l):
	c, v = l.strip().split()
	i = int(v)
	if c == 'forward':
		return (p[0] + i, p[1], p[2] + p[1] * i)
	elif c == 'up':
		return (p[0], p[1] - i, p[2])
	else: # c == 'down':
		return (p[0], p[1] + i, p[2])

pos = reduce(f, open('2.input'), (0, 0, 0))

print(f"a: {pos[0]} * {pos[1]} = {pos[0] * pos[1]}")
print(f"b: {pos[0]} * {pos[2]} = {pos[0] * pos[2]}")





pos = (0, 0, 0)

for line in open('2.input'):
	cmd, val = line.strip().split()
	ival = int(val)
	if cmd == 'forward':
		pos = (pos[0] + ival, pos[1], pos[2] + pos[1] * ival)
	elif cmd == 'up':
		pos = (pos[0], pos[1] - ival, pos[2])
	else: # cmd == 'down':
		pos = (pos[0], pos[1] + ival, pos[2])

print(f"a: {pos[0]} * {pos[1]} = {pos[0] * pos[1]}")
print(f"b: {pos[0]} * {pos[2]} = {pos[0] * pos[2]}")
