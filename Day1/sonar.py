x = []

with open(r'./Day1/sonar.txt', 'r') as f:
    content = f.readlines()
    x = content[0]

cnt = 0
for txt in content[1:]:
    if int(txt) > x:
        cnt += 1
    x = txt

print(cnt)

    