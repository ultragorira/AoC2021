with open(r'./Day1/sonar.txt', 'r') as f:
    DATA = [int(x) for x in f.readlines()]


def part_one(data=DATA):
    return sum(1 if data[x] > data[x - 1] else 0 for x in range(1, len(data)))


print(part_one())