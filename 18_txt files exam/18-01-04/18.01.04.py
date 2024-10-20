with open("words.txt", "r", encoding="utf-8") as f:
    _data = "".join(f.readlines()).split()
    [print(i) for i in _data if len(i) == len(max(_data, key=len))]