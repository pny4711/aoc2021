def is_foldx(x, fa, fn): return (fa == 'x' and x > fn)
def is_foldy(y, fa, fn): return (fa == 'y' and y > fn)
def is_fold(x, y, fa, fn): return is_foldx(x, fa, fn) or is_foldy(y, fa, fn)
def fold(x, y, fa, fn):
    return (fn - (x - fn) if is_foldx(x, fa, fn) else x, 
            fn - (y - fn) if is_foldy(y, fa, fn) else y)

nr_dots,dots = [], set()
with open('13.input.txt') as f:
    for line in f:
        if line.strip() == '':
            break
        x,y = line.strip().split(',')
        dots.add((int(x),int(y)))

    for fl in [line.strip() for line in f]:
        fa,fn = fl.split()[2].split('=')
        fn = int(fn)
        dots = set([fold(x, y, fa, fn)  for x, y in dots 
                    if not is_fold(x, y, fa, fn) or fold(x, y, fa, fn) not in dots])
        nr_dots.append(len(dots))

print(f"a: {nr_dots[0]}\n")
for y in range(1+ max([y for _,y in dots])):
    print("".join(['#' if (x,y) in dots else ' ' 
                    for x in range(1+ max([x for x,_ in dots]))]))