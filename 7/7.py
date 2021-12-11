import os
os.chdir(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))))

pl = [int(x) for line in open('7.input.ref') for x in line.strip().split(',')]

dummy = [x for x in range(max(pl) + 1)]
costtable = [0]
for x in range(1,max(pl) + 1):
	costtable.append(costtable[-1] + x)

best_a = None
best_b = None

for a in range(min(pl), max(pl)):
	fuel_a = sum([abs(a-x) for x in pl])
	fuel_b = sum([costtable[abs(a-x)] for x in pl])
	if not best_a or best_fuel_a > fuel_a:
		best_a = a
		best_fuel_a = fuel_a
	if not best_b or best_fuel_b > fuel_b:
		best_b = a
		best_fuel_b = fuel_b

print(f"a: {best_fuel_a} @ {best_a}")
print(f"b: {best_fuel_b} @ {best_b}")

print(f"a: {min([sum([abs(a - x) for x in pl]) for a in range(max(pl))])}")
print(f"b: {min([sum([costtable[abs(a - x)] for x in pl]) for a in range(max(pl))])}")
