gamma = ''
epsylon = ''
width = 0
tot_0 = 0
tot_1 = 0

input = [line.strip() for line in open(r'./Day3/input.txt')]
width = len(input[0])
print(width)

for i in range (0, width):
    for item in input:
        tot_0 += 1 if int(item[i]) == 0 else 0
        tot_1 += 1 if int(item[i]) == 1 else 0
    gamma += '0' if tot_0 > tot_1 else '1'
    epsylon += '0' if tot_0 < tot_1 else '1'
    tot_0 = 0
    tot_1 = 0

print(int(gamma, 2))
print(int(epsylon, 2))
print(int(gamma, 2)*int(epsylon,2))


    



