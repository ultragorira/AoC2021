data = [int(x) for x in open(r'./Day7/in.txt').read().strip().split(',')]
k = list(map(int, data))

q = float("inf")

g = lambda x: x * (x + 1) // 2

for i in range(min(k), max(k) + 1):
    t = sum(g(abs(x - i)) for x in k)
    q = min(q, t)

print(q)

