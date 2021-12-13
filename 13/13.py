def fold(x, y, fa, fn):
    return (fn - (x - fn) if (fa == 'x' and x > fn) else x, 
            fn - (y - fn) if (fa == 'y' and y > fn) else y)

nr_dots = []
lines,folds = open('13.input.txt').read().split('\n\n')
dots = set([(int(i) for i in l.split(',')) for l in lines.strip().split('\n')])

for fl in folds.strip().split('\n'):
    fa,fn = fl.split()[2].split('=')
    dots = set([fold(x, y, fa, int(fn))  for x, y in dots])
    nr_dots.append(len(dots))

print(f"a: {nr_dots[0]}\n")
for y in range(1+ max([y for _,y in dots])):
    print("".join(['#' if (x,y) in dots else ' ' 
                    for x in range(1+ max([x for x,_ in dots]))]))