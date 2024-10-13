txt = list(map(int, input().replace(".", "").replace("-", "")))
print(max(txt) + min(txt))