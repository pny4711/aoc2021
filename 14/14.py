line,rulelines = open('14.input').read().split('\n\n')
rules = {}
for l in rulelines.strip().split('\n'):
    pair, insert = l.split('->')
    rules[pair.strip()] = insert.strip()

cache = {}

def merge(d0, d, extra):
    for ch, n in d:
        if ch not in d0:
            d0[ch] = 0
        d0[ch] += n - 1 if ch == extra else n

def expand_pair(times, pair):
    if times == 0: 
        return {pair[0]:2} if pair[0] ==pair[1] else {pair[0]:1, pair[1]:1}
    if (times,pair) in cache: 
        return cache[(times,pair)]
    extra = rules[pair]
    data = {ch:v for ch,v in expand_pair(times-1, pair[0] + extra).items()}
    merge(data, expand_pair(times-1, extra + pair[1]).items(), extra)        
    cache[(times,pair)] = data
    return data

def expand(times, s):
    res = {line[0]:1}
    for i in range(len(s) - 1):
        merge(res, expand_pair(times, line[i] + line[i + 1]).items(), line[i])
    return res

vals1 = sorted([v for v in expand(10, line).values()])
print(f"a: {vals1[-1] - vals1[0]}")
vals2 = sorted([v for v in expand(40, line).values()])
print(f"b: {vals2[-1] - vals2[0]}")