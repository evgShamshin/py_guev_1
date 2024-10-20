file = input()

with open(file, "r", encoding="utf-8") as f:
    print(len([line for line in f]))