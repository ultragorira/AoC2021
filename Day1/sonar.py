stack = []

with open(r'./Day1/sonar.txt', 'r') as f:
    content = f.readlines()
    stack.append(content[0])

cnt = 0
for txt in content[1:]:
    if int(txt) > int(stack[0]):
        cnt += 1
        stack.pop()
        stack.append(txt)
    else:
        stack.pop()
        stack.append(txt)

print(cnt)

    