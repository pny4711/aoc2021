
map = {}

def insert(m, a, b):
    if a != 'end' and b != 'start':
        if a in m:
            m[a].append(b)
        else:
            m[a] = [b]

for a,b in [line.strip().split('-') for line in open('12.input.txt')]:
    insert(map, a, b)
    insert(map, b, a)

def walk(map, path, seen_small_once, seen_small_twice):
    paths = []
    for next in map[path[-1]]:
        if next == "end":
            paths += [path + [next]]
        elif next.isupper():
            paths += walk(map, path + [next], seen_small_once, seen_small_twice)
        elif next not in seen_small_once:
            paths += walk(map, path + [next], seen_small_once + [next], seen_small_twice)
        elif not seen_small_twice:
            paths += walk(map, path + [next], seen_small_once + [next], True)
    return paths

paths1 = walk(map, ["start"], [], True)
print(f"a: {len(paths1)}")
paths2 = walk(map, ["start"], [], False)
print(f"b: {len(paths2)}")
