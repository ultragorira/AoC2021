inp = [int(x) for x in open(r'./Day6/in.txt').read().strip().split(',')]
for _ in range(80):
    Y = []
    for x in inp:
        if x == 0:
            Y.append(6)
            Y.append(8)
        else:
            Y.append(x-1)
    inp = Y

print(len(inp))
