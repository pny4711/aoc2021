import functools
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

class parse_exception(BaseException):
	def __init__(self, ch):
		self.ch = ch

pp = {'(':')', '{':'}','[':']','<':'>'}

score = {')': (3, 1), ']': (57, 2), '}': (1197, 3), '>': (25137, 4)}

sca = 0
scb = []

def p(line):
	debt = ""
	while line:
		if debt and line[0] == debt[0]:
			line, debt = line[1:], debt[1:]
		elif line and line[0] in pp:
			line, debt = line[1:], pp[line[0]] + debt
		else:
			raise parse_exception(line[0])
	return debt

for line in open(os.path.join(__location__, '10.input.txt')):
	try:
		scb.append(functools.reduce(lambda v,ch: v * 5 + score[ch][1], p(line.strip()), 0))
	except parse_exception as e:
		sca += score[e.ch][0]

print(f"a:{sca}")
print(f"b:{sorted(scb)[len(scb) // 2]}")


