import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
flag = "НЕТ"
print(lst_in)
for i in range(len(lst_in))[1:-1]:
    for j in range(len(lst_in))[1:-1]:
        if int(lst_in[i]) * int(lst_in[j]) == int(lst_in[-1]) and i != j:
            flag = "ДА"
            break

print(flag)