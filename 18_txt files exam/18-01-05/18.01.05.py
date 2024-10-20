file = input()

with open(file, "r", encoding="utf-8") as f:
    l = [line.strip() for line in f]
    print(*l[-10:], sep="\n") if len(l) > 10 else print(*l, sep="\n")