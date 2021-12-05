width = 0
tot_0 = 0
tot_1 = 0
index_to_delete = []

input = [line.strip() for line in open(r'./Day3/input.txt')]
input2 = input
width = len(input[0])
print(width)

for i in range (0, width):
    for item in input:
        tot_0 += 1 if int(item[i]) == 0 else 0
        tot_1 += 1 if int(item[i]) == 1 else 0
    if tot_0 > tot_1:
        for item in input:
            if int(item[i]) == 1:
                index_to_delete.append(item)
    elif tot_1 > tot_0 or tot_1 == tot_0:
        for item in input:
            if int(item[i]) == 0:
                index_to_delete.append(item)
    tot_0 = 0
    tot_1 = 0
    if len(input)>1:
        input = list(set(input) - set(index_to_delete))
    
    index_to_delete.clear()

for i in range (0, width):
    for item in input2:
        tot_0 += 1 if int(item[i]) == 0 else 0
        tot_1 += 1 if int(item[i]) == 1 else 0
    if tot_0 > tot_1:
        for item in input2:
            if int(item[i]) == 0:
                index_to_delete.append(item)
    elif tot_1 > tot_0 or tot_1 == tot_0:
        for item in input2:
            if int(item[i]) == 1   :
                index_to_delete.append(item)
    tot_0 = 0
    tot_1 = 0
    if len(input2)>1:
        input2 = list(set(input2) - set(index_to_delete))
    
    index_to_delete.clear()


print(input)
print(input2)
print(int(input[0], 2)*int(input2[0],2))