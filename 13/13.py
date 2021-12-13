def is_foldx(x, fa, fn): return (fa == 'x' and x > fn)
def is_foldy(y, fa, fn): return (fa == 'y' and y > fn)
def is_fold(x, y, fa, fn): return is_foldx(x, fa, fn) or is_foldy(y, fa, fn)
def fold(x, y, fa, fn):
    return (fn - (x - fn) if is_foldx(x, fa, fn) else x, 
            fn - (y - fn) if is_foldy(y, fa, fn) else y)

nr_dots = []
lines,folds = open('13.input.txt').read().split('\n\n')
dots = set([(int(i) for i in l.split(',')) for l in lines.strip().split('\n')])

for fl in folds.strip().split('\n'):
    fa,fn = fl.split()[2].split('=')
    fn = int(fn)
    dots = set([fold(x, y, fa, fn)  for x, y in dots 
                if not is_fold(x, y, fa, fn) or fold(x, y, fa, fn) not in dots])
    nr_dots.append(len(dots))

print(f"a: {nr_dots[0]}\n")
for y in range(1+ max([y for _,y in dots])):
    print("".join(['#' if (x,y) in dots else ' ' 
                    for x in range(1+ max([x for x,_ in dots]))]))