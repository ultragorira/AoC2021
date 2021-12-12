from collections import Counter, defaultdict

inp = Counter([int(x) for x in open(r'./Day6/in.txt').read().strip().split(',')])

for day in range(256):
    Y = defaultdict(int)
    for x, count in inp.items():
        if x == 0:
            Y[6] +=count
            Y[8] +=count
        else:
            Y[x-1] += count
    inp = Y

print (sum(inp.values()))