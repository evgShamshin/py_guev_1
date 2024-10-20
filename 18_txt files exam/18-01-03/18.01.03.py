with open("grades.txt", "r", encoding="utf-8") as f:
    l = [l.split() for l in f]
    count = 0
    temp = 0

    for i in l:

        for j in i[1:]:
            if int(j) >= 65: temp += 1

        if temp == 3: count += 1
        temp = 0

    print(count)