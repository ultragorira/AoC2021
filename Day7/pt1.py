data = [int(x) for x in open(r'./Day7/in.txt').read().strip().split(',')]
k = list(map(int, data))

q = float("inf")

for i in range(min(k), max(k) + 1):
    t = sum(abs(x - i) for x in k)
    q = min(q, t)

print(q)

#ELSE get median after sorting 

data.sort()
result = 0

med = data[len(data)//2]
for x in data:
    result += abs(x-med)
print(result)