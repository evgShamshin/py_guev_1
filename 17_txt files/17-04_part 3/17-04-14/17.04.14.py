def time_check(_1, _2):
    _1 = list(map(int, _1.split(":")))
    _2 = list(map(int, _2.split(":")))
    if abs(_1[0] - _2[0]) > 1:
        return True
    elif abs(_1[0] - _2[0]) == 1 and _1[1] - _2[1] <= 0:
        return True
    else:
        return False


with open("logfile.txt", "r", encoding="utf-8") as logfile, open("output.txt", "w", encoding="utf-8") as output:
    data_log = [list(map(lambda x: str(x).rstrip(), i.split(", "))) for i in logfile]
    data_out = [i[0] for i in data_log if time_check(i[1], i[2])]
    output.write("\n".join(data_out))
