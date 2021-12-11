lines = [[[x for x in y.split()] for y in l.strip().split('|')] for l in open("8.input.txt")]

print(f"a: {sum([len([x for x in l[1] if len(x) in (2, 3, 4, 7)]) for l in lines])}")

all_numbers = ['abcefg','cf','acdeg','acdfg','bcdf',
			   'abdfg','abdefg','acf','abcdefg','abcdfg']
all_segments = ('a','b','c','d','e','f','g')

sum = 0

for signals, numbers in lines:
	translation =  {ch:set(all_segments) for ch in all_segments}

	test_numbers = signals + numbers

	def filter(nr, possible):
		for ch in nr:
			translation[ch] = translation[ch].intersection(possible)

	def get_digit(mapping, num):
		xnum = "".join(sorted([mapping[x] for x in num]))
		return all_numbers.index(xnum)

	def remove_impossible():

		def is_valid(m):
			for p in test_numbers:
				try:
					get_digit(m, p)
				except:
					return False
			return True

		def get_mappings():
			return [{'a': xa, 'b': xb, 'c': xc, 'd':xd, 'e': xe, 'f': xf, 'g': xg }
					for xa in translation['a']
					for xb in translation['b'] if xb != xa
					for xc in translation['c'] if xc not in [xa,xb]
					for xd in translation['d'] if xd not in [xa,xb,xc]
					for xe in translation['e'] if xe not in [xa,xb,xc,xd]
					for xf in translation['f'] if xf not in [xa,xb,xc,xd,xe]
					for xg in translation['g'] if xg not in [xa,xb,xc,xd,xe,xf]]

		def try_xch(ch, xch):
			for m in get_mappings():
				if m[ch] == xch and is_valid(m):
					return True
			return False

		for tch, cand in translation.items():
			if len(cand) > 1:
				for xch in [xch for xch in cand if not try_xch(tch, xch)]:
					translation[tch].remove(xch)

	for p in test_numbers:
		if len(p) == 2:
			 	filter(p, set(['c','f']))
		elif len(p) == 3:
				filter(p, set(['a','c','f']))
		elif len(p) == 4:
				filter(p, set(['b','c','d','f']))

	remove_impossible()

	m = {k:list(x)[0] for k,x in translation.items()}

	val = 0
	for n in numbers:
		val = val * 10 + get_digit(m, n)

	sum += val

print(f"b: {sum}")

