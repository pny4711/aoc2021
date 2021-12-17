
def try_velocity(xt,yt,target):
    xti,yti = xt,yt
    xl,xh,yl,yh = target

    x,y = 0,0

    ymax = 0

    while True:
        x = x + xt
        y = y + yt
        if xt > 0:
            xt -= 1
        elif xt < 0:
            xt += 1
        yt -= 1

        ymax = max(y,ymax)

        if y < yl:
            return False, 0, 1

        if xt == 0 and x < xl:
            return False, 0, 2
 
        if yl <= y <= yh and xl <= x <= xh:
                return True, ymax, 0
 
        if x > xh:
            if yt > 0:
                return False, 0, 3
            if xt > y - yl:
                return False, 0, 4

a = 0
b = 0

#t = (20,30,-10,-5)      # Sample
t = (236,262,-78,-58)    # Input

failstats= [0,0,0,0,0,0]

for xt in range(1,t[1]+1):
    for yt in range(t[2],t[1]+1):
        s,m,f = try_velocity(xt,yt,t)
        if s:
#            print(f"  Hit: {xt},{yt} -> {m}")
            a = max(a,m)
            b += 1
        failstats[f] += 1

print(f"a: {a}")
print(f"a: {b}")

print(f"Fail stats: {failstats}")