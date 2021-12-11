import os
os.chdir(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))))

import time

seen = {}

def nrfad(days,nr):
	global seen
	if (days,nr) not in seen:
		fd = [1,0,0,0,0,0,0,0,0]
		for i in range(days - nr):
			fd = fd[1:7] + [fd[7] + fd[0]] + [fd[8]]+ [fd[0]]
		seen[(days,nr)] = sum(fd)
	return seen[(days,nr)]

start = time.time()

print(f"a: {sum([nrfad(80,f)  for f in [int(sf) for l in open('6.input') for sf in l.strip().split(',')]])}")
print(f"b: {sum([nrfad(256,f) for f in [int(sf) for l in open('6.input') for sf in l.strip().split(',')]])}")

print(f"Time: {time.time() - start}")