with open("ledger.txt", "r", encoding="utf-8") as f:
    print(f"${sum(list(map(lambda x: int(x[1:]), [line for line in f])))}")