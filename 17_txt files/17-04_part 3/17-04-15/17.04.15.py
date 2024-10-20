def read_csv():
    with open("data.csv", encoding="utf-8") as csv:
        key = [line.strip() for line in csv.readline().split(',')]
        value = [line.strip().split(',') for line in csv.readlines()]
    return[dict(zip(key, i)) for i in value]

print(read_csv())