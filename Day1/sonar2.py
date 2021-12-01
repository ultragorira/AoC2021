with open(r'./Day1/sonar.txt', 'r') as f:
    file_cont = [int(x) for x in f.readlines()]


def count_increase(data=file_cont):
    return sum(1 if data[x] > data[x - 1] else 0 for x in range(1, len(data)))

def triple_measure():
    return count_increase(
        [file_cont[x] + file_cont[x - 1] + file_cont[x - 2] for x in range(len(file_cont)) if x >= 2]
    )

print(count_increase())
print(triple_measure())