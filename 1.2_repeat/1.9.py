number = input()
l = []
res = ""
temp = 0
total = []

for num in number:
    l.append(num)

for i in range(1, len(l) + 1):
    temp += 1
    if temp == 3:
        temp = 0
        total.append(l[-i])
        total.append(",")
    else:
        total.append(l[-i])

for i in range(1, len(total) + 1):
    res += (total[-i])

if res[0] == ',':
    res = res[1:]

print(res)