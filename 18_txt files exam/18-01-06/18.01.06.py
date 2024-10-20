file = input()

with open(file, encoding="utf-8") as f, open("forbidden_words.txt", encoding="utf-8") as fw:
    s_rep = fw.read().split()
    res = []
    for s in f:
        for x in s_rep:
            while x in s:
                index = s.lower().index(x)
                s = s[:index] + "*" * len(x) + s[index + len(x):]
        res.append(s)
print(*res)
