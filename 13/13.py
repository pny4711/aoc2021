maxx,maxy = 0,0
dots = []
nrdots = None
with open('13.input.txt') as f:
    for line in f:
        if line.strip() == '':
            break
        x,y = line.strip().split(',')
        dots.append((int(x),int(y)))
        maxx = max(int(x),maxx)
        maxy = max(int(y),maxy)

    fold = [line.strip() for line in f]

w = [[' ' for x in range(maxx +1)] for y in range(maxy + 1)]
for x,y in dots:
    w[y][x] = '#'

for fl in fold:
    fa,fn = fl.split()[2].split('=')
    fn = int(fn)

    if fa == 'y':
        w1 = w[-1:fn:-1]
        w0 = w[:fn]
    else:
        w1 = [wl[-1:fn:-1] for wl in w]
        w0 = [wl[:fn] for wl in w]
 
    w = [[v if v == '#' else w0[y][x] for x,v in enumerate(w1l)] for y, w1l in enumerate(w1)]

    if not nrdots:
        nrdots = sum([1 for l in w for v in l if v == '#'])
        print(f"a: {nrdots}\n")

print("\n".join(["".join(l) for l in w]))