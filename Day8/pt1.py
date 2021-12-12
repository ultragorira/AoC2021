tot = 0

for k in open('./Day8/in.txt'):
    a, b = k.strip().split(" | ")
    for j in b.split():
        if len(j) in [2, 3, 4, 7]:
            tot += 1

print(tot)