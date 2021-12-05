
h = 0
d = 0 
aim = 0

for line in open(r'./Day2/input.txt'):    
    h=h+int(line.strip().split(' ')[1]) if len(line.strip().split(' ')[0]) == 7 else h
    d=d+int(line.strip().split(' ')[1]) if len(line.strip().split(' ')[0]) == 4 else d
    d=d-int(line.strip().split(' ')[1]) if len(line.strip().split(' ')[0]) == 2 else d

print(h*d)

h = 0
d = 0

for line in open(r'./Day2/input.txt'):    
    h=h+int(line.strip().split(' ')[1]) if len(line.strip().split(' ')[0]) == 7 else h
    aim=aim+int(line.strip().split(' ')[1]) if len(line.strip().split(' ')[0]) == 4 else aim
    aim=aim-int(line.strip().split(' ')[1]) if len(line.strip().split(' ')[0]) == 2 else aim
    d = d+aim*int(line.strip().split(' ')[1]) if len(line.strip().split(' ')[0])==7 else d
    
print(aim)
print(h)
print(d)

print(h*d)