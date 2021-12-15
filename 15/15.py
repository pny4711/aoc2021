
def find_cr(risc):

    size = len(risc)
    cr = [[0 for x in range(size)] for y in range(size)]
    for i in range(1, size):
        cr[i][0] = cr[i-1][0] + risc[i][0]
        cr[0][i] = cr[0][i-1] + risc[0][i]

    for y in range(1,size):
        for x in range(1,size):
            cr[y][x] = min(cr[y-1][x],cr[y][x-1]) + risc[y][x]

    last = size -1

    for y in range(1,size):
        for x in range(1,size):
            wl = []
            r = cr[y][x]
            rn = r + risc[y-1][x]
            if cr[y-1][x] > rn:
                cr[y-1][x] = rn
                wl += [(y-1,x)]

            rn = r + risc[y][x-1]
            if cr[y][x-1] > rn:
                cr[y][x-1] = rn
                wl += [(y,x-1)]

            while wl:

                wy,wx = wl.pop(0)
                r = cr[wy][wx]

                if 0 < wy:
                    rn = r + risc[wy-1][wx]
                    if cr[wy-1][wx] > rn:
                        cr[wy-1][wx] = rn
                        wl += [(wy-1,wx)]

                if 0 < wx:
                    rn = r + risc[wy][wx-1]
                    if cr[wy][wx-1] > rn:
                        cr[wy][wx-1] = rn
                        wl += [(wy,wx-1)]

                if wy < last:
                    rn = r + risc[wy+1][wx]
                    if cr[wy+1][wx] > rn:
                        cr[wy+1][wx] = rn
                        wl += [(wy+1,wx)]

                if wx < last:
                    rn = r + risc[wy][wx+1]
                    if cr[wy][wx+1] > rn:
                        cr[wy][wx+1] = rn
                        wl += [(wy,wx+1)]    
    return cr
    
riska = [[int(r) for r in line.strip()] for line in open('15.input')]
cra = find_cr(riska)
print(f"a: {cra[len(riska) - 1][len(riska) - 1]}")

def wr(r): return r if r < 10 else r - 9
riskb = [[wr(riska[y][x] + ex + ey) for ex in range(5) for x in range(len(riska))]
            for ey in range(5) for y in range(len(riska))]

crb = find_cr(riskb)
print(f"a: {crb[len(riskb) - 1][len(riskb) - 1]}")

