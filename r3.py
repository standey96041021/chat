lines=[]
with open('message_with_r3.txt', 'r', encoding = 'utf-8-sig') as f:
    for line in f:
        lines.append(line.strip())
    #print(lines)
for line in lines:
    s = line.split(' ')
    name = s[2][5:]
    print(name)